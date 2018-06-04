from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from flask import flash, redirect, url_for
from werkzeug.routing import BuildError
from slugify import slugify
from datetime import datetime


class User(UserMixin, db.Model):
    """
    Create an Users table
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    profile_pic = db.Column(db.String())
    password_hash = db.Column(db.String(128))
    campgrounds = db.relationship('Campground', backref='user_campground', lazy='dynamic')
    comment = db.relationship('Comment', backref='user_comment', lazy='dynamic')
    is_admin = db.Column(db.Boolean, default=False)
    confirm_email = db.Column(db.Boolean, default=False)
    confirm_on = db.Column(db.DateTime, index=True)

    @property
    def password(self):
        """
        Avoid password from being accessed
        """
        raise AttributeError(" Passworty can't be accessed")

    @password.setter
    def password(self, password):
        """
        Set a hash password
        """
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        """
        Verify if password matches actual password
        """
        return check_password_hash(self.password_hash, password)

# Set up user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_handler():
    flash('You must be login to perform this action', 'danger')
    return redirect(url_for('auth.user_login'))


class Campground(db.Model):
    """
    Create a campground table

    """
    __tablename__ = "campgrounds"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), index=True)
    image = db.Column(db.String())
    lat = db.Column(db.Integer())
    lng = db.Column(db.Integer)
    price = db.Column(db.DECIMAL)
    location = db.Column(db.String())
    description = db.Column(db.String())
    image_id = db.Column(db.String())
    create_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref="campground_comment", lazy='dynamic')


    @property
    def slugified_name(self):
        return slugify(self.name, separator="-")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    create_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    campground_id = db.Column(db.Integer, db.ForeignKey('campgrounds.id'))
