from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user
from . import auth
from . forms import LoginForm, RegistrationForm

from .. models import User
from app import db

@auth.route('/register', methods=['POST', 'GET'])
def register_user():
    """
    Handles user registration at /register
    """
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        new_user = User(email=registration_form.email.data, username=registration_form.username.data,
                    first_name=registration_form.first_name.data, last_name=registration_form.last_name.data,
                    profile_pic=registration_form.profile_pic.data,
                    password=registration_form.password.data)
                    
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered. You may now login', 'success')
        return redirect(url_for('auth.user_login'))
    
    return render_template('auth/register.html', registration_form=registration_form, title="Register")


@auth.route('/login', methods=['POST', 'GET'])
def user_login():
    """
    Handles user login at /account/login
    """
    login_form = LoginForm()
    if login_form.validate_on_submit():
        register_user = User.query.filter_by(email=login_form.email.data).first()
        if register_user is not None and register_user.verify_password(login_form.password.data):
            login_user(register_user)
            return redirect(url_for('home.home_page'))
    
        else:
            flash("Invalid Credentials. Please provide valid credential to login.", 'danger')
            return redirect(url_for('auth.user_login'))
    
    return render_template('auth/login.html', login_form=login_form, title="Login")
    
    
@auth.route('/logout')
def user_logout():
    """
    Handles logout for current login users
    """
    flash(current_user.username + ', you have succesfully logout', 'success')
    logout_user()
    
    return redirect(url_for('auth.user_login'))