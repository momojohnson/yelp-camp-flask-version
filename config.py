import os
import cloudinary as Cloud

class Config(object):
    """
    Common configurations
    """

class DevelopmentConfig(Config):
    """
    Development Configurations
    """
    # CLOUDINARY_CLOUD_NAME=diuj5cx43
    # CLOUDINARY_API_KEY=914652556944178
    # CLOUDINARY_API_SECRET=yhybjSs4aWabQWwVa1pjkjFgImA
    Cloud.config.update = ({
    'cloud_name':os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'api_key': os.environ.get('CLOUDINARY_API_KEY'),
    'api_secret': os.environ.get('CLOUDINARY_API_SECRET')
    })
    # api_key = os.environ.get('api_key')
    # cloud_name = os.environ.get('cloud_name')

    # api_secret = os.environ.get('api_secret')
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production Configurations
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False



app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
