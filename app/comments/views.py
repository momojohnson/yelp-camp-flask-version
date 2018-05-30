from flask import flash, redirect, render_template, url_for
from flask_login import login_required, current_user
from . import comments

from . forms import CommentForm
from ..models import Campground, Comment, User
from app import db

@comments.route('/add')
def add_comment(slug, campground_id):
    console.log(slug)
    return str(campground_id)
