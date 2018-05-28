from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment


from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)
    
    from app import models
    
    from . home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    from . admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    
    from . auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/account")
    
    from . campgrounds import campground as campgrounds_blueprint
    app.register_blueprint(campgrounds_blueprint, url_prefix="/campgrounds")
    
    from . comments import comments as comments_blueprint
    app.register_blueprint(comments_blueprint, url_prefix="/comments")
    
    return app