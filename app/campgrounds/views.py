from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user, login_manager
from decorators import check_confirmed
import geocoder

from .. models import Campground, Comment, User
from app import db

from . import campground
from . forms import CampgroundForm

@campground.route('/')
def list_all_campgrounds():
    """
    Show all campgrounds at route /campgrounds/
    """
    campgrounds = Campground.query.all()
    return render_template('campgrounds/list_campgrounds.html', campgrounds=campgrounds, title="Campgrounds")

@campground.route('/add', methods=['GET','POST'])
@login_required
@check_confirmed
def create_campground():
    add_campground = True
    user = User.query.get(current_user.id)
    campground_form = CampgroundForm()
    if campground_form.validate_on_submit():
            campground = Campground(name=campground_form.name.data, image=campground_form.image.data,
                        price=campground_form.price.data,
                        description=campground_form.description.data,
                        user_campground=user)
            g = geocoder.google(campground_form.location.data)
            campground.location = g.json.get('raw').get('formatted_address')
            campground.lat= g.json.get('raw').get('geometry').get('location').get('lat')
            campground.lng = g.json.get('raw').get('geometry').get('location').get('lng')
            db.session.add(campground)
            db.session.commit()
            return redirect(url_for('campground.list_all_campgrounds'))

    return render_template('campgrounds/campground.html', campground_form=campground_form, add_campground=add_campground, title="New Campground")



@campground.route('/<int:campground_id>/<slug>')
def display_campground(campground_id, slug):
    """
    Show a particular campground at route /campgrounds/campground_id/<slug>
    """
    campground = Campground.query.get_or_404(campground_id)

    return render_template('campgrounds/show_campground.html', campground=campground, title=campground.name)



@campground.route('/<int:campground_id>/<slug>/edit', methods=['GET', 'POST'])
@login_required
@check_confirmed
def edit_campground(campground_id, slug):

    """
    Edit a campground at route /campgrounds/campground_id/<slug>/edit
    """
    add_campground = False
    campground = Campground.query.get_or_404(campground_id)
    campground_form = CampgroundForm(obj=campground)
    if campground_form.validate_on_submit():
        campground.name = campground_form.name.data
        campground.image = campground_form.image.data
        g = geocoder.google(campground_form.location.data)
        campground.location = g.json.get('raw').get('formatted_address')
        campground.lat= g.json.get('raw').get('geometry').get('location').get('lat')
        campground.lng = g.json.get('raw').get('geometry').get('location').get('lng')
        campground.price = campground_form.price.data
        campground.description = campground_form.description.data
        db.session.commit()
        return redirect(url_for('campground.display_campground', campground_id=campground.id, slug=campground.slugified_name))

    return render_template('campgrounds/campground.html', campground_form=campground_form, add_campground=add_campground, campground=campground)

@campground.route('/<int:campground_id>/<slug>/delete', methods=['GET','POST'])
@login_required
@check_confirmed
def delete_campground(campground_id, slug):
    """
    Delete a campground at route /campgrounds/campground_id/<slug>/delete
    """
    campground = Campground.query.get_or_404(campground_id)
    campground_name = campground.name
    db.session.delete(campground)
    db.session.commit()
    flash(campground_name + ' has been successfully deleted', 'success')
    return redirect(url_for('campground.list_all_campgrounds'))
