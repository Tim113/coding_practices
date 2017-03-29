import os
import logging

# See more information about Flask Config at:
# http://flask.pocoo.org/docs/0.10/config/
conf_root_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(conf_root_dir, os.pardir))

# General Parameters
class Config(object):
    DEBUG = True
    TESTING = False
    HOST = '0.0.0.0'
    APP_DIR = root_dir
    APP_DEBUG = True
    # GENERAL_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    # Flask-Security Config
    # WTF_CSRF_ENABLED = True
    SECRET_KEY = 'c00qfyR8_T8Nsu4AIUUIzJPUxasvcUeYzplgSLHqkzWuKe3Y1a6pPQ0pgbgK06AC'
    
    # DATABASE_URL CONNECTION STRING
    RDS_DB_TYPE = os.getenv('RDS_BD_TYPE','postgresql')
    RDS_DB_NAME = os.getenv('RDS_DB_NAME','app_name')
    RDS_USERNAME  = os.getenv('RDS_USERNAME','your_username')
    RDS_PASSWORD  = os.getenv('RDS_PASSWORD','your_password')
    RDS_HOSTNAME  = os.getenv('RDS_HOSTNAME','localhost:5432')
    RDS_PORT = os.getenv('RDS_PORT','5432')

    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}/{}'.format(RDS_DB_TYPE,RDS_USERNAME,RDS_PASSWORD,RDS_HOSTNAME,RDS_DB_NAME)

    # Flask-Security features
    SECURITY_REGISTERABLE = True
    
class ProductionConfig(Config):

    LOGGER_LEVEL = logging.WARN
    LOGGER_FILE = os.path.join(root_dir, 'logs/production.log')


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'

    # Logging
    LOGGER_LEVEL = logging.DEBUG
    LOGGER_FILE = os.path.join(root_dir, 'logs/development.log')


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig
}
