import os
import configparser
from app import app

## Init logging config ===
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

def getAppConfig():
    config = configparser.ConfigParser()

    PREFIX = '-debug' if app.config['DEBUG'] else ''
    APPCONFIG_FILENAME = 'appconfig{}.ini'.format(PREFIX)

    configpath = os.path.join(os.path.dirname(__file__), '../config', APPCONFIG_FILENAME)
    config.read(configpath)
    return config
