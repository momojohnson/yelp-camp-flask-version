

class Config(object):
    """
    Common configurations
    """

class DevelopmentConfig(Config):
    """
    Development Configurations
    """
    
    SQLALCHEMY_ECHO = True
    DEBUG = True
    
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