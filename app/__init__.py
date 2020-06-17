import configparser
from flask import Flask
import logging

APPNAME = 'FlaskRESTX-webapi'

app = Flask(APPNAME)

# general
App.config['VERSION'] = 'v1'
App.config['DESCR'] = "A blueprint to design Python API using Flask-RESTX"
App.config['RESTX_MASK_SWAGGER'] = False

# config (e.g.: mysql)
from .core.configs import getAppConfig
appcfg = getAppConfig()

App.config['MYSQL_DATABASE_USER'] = appcfg['DB']['MYSQL_DATABASE_USER']
App.config['MYSQL_DATABASE_PASSWORD'] = appcfg['DB']['MYSQL_DATABASE_PASSWORD']
App.config['MYSQL_DATABASE_DB'] = appcfg['DB']['MYSQL_DATABASE_DB']
App.config['MYSQL_DATABASE_HOST'] = appcfg['DB']['MYSQL_DATABASE_HOST']
App.config['MYSQL_DATABASE_PORT'] = int(appcfg['DB']['MYSQL_DATABASE_PORT'])


logging.info(App.config)

import app.core.database
import app.apis
