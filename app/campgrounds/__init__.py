from flask import Blueprint

campground = Blueprint('campground', __name__)

from . import views