from flask import render_template
from . import home

@home.route('/')
def home_page():
    return render_template('home/index.html', title="Home")