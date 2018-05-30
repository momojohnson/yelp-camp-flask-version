

class Config(object):
    """
    Common configurations
    """

class DevelopmentConfig(Config):
    """
    Development Configurations
    """
    
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