from . import comments
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from .. models import Campground, Comment, User
from . forms import commentForm
from app import db

@comments.route('/add', methods=['GET', 'POST'])
@login_required
def add_comment(slug, campground_id):
    """
    Handles comment creation at /campgrounds/campground_id>/<slug>/comment/add
    Associate a particular comment with the user that created the comment
    as well as the campground for which the comment was was created.
    
    redirect to /campground/<slug/campground_id
    
    """
    add_comment = True
    campground = Campground.query.get_or_404(campground_id)
    user = User.query.get_or_404(current_user.id)
    comment_form = commentForm()
    if comment_form.validate_on_submit():
        comment = Comment(comment=comment_form.comment.data,
                         user_comment=user,
                         campground_comment=campground)
        db.session.add(comment)
        db.session.commit()
        flash('Comment for {} successfully added'.format(campground.name), 'success')
        return redirect(url_for('campground.display_campground', slug=campground.slugified_name, campground_id=campground.id ))
    
    
    return render_template('comments/create_comment.html', comment_form=comment_form, campground=campground, add_comment=add_comment, title='Create Comment')
    
@comments.route('/<int:comment_id>/edit', methods=['GET', 'POST'])
def edit_comment(slug, campground_id, comment_id):
    """
    Handles editing of a user comment at route /campgrounds/campground_id>/<slug>/comment/comment_id/edit
    
    """
    add_comment = False
    campground = Campground.query.get_or_404(campground_id)
    comment = Comment.query.get_or_404(comment_id)
    comment_form = commentForm(obj=comment)
    if comment_form.validate_on_submit():
        comment.comment = comment_form.comment.data
        db.session.commit()
        return redirect(url_for('campground.display_campground', slug=campground.slugified_name, campground_id=campground.id))
    
    return render_template('comments/create_comment.html', campground=campground, comment_form=comment_form, comment=comment, add_comment=add_comment, title="Edit Comment")

@comments.route('/<int:comment_id>/delete', methods=['GET', 'POST'])
def delete_comment(slug, campground_id, comment_id):
    campground = Campground.query.get_or_404(campground_id)
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('campground.display_campground', slug=campground.slugified_name, campground_id=campground.id))
    