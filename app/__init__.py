import configparser
from flask import Flask
import logging

APPNAME = 'FlaskRESTX-webapi'

app = Flask(APPNAME)

# general
app.config['VERSION'] = 'v1'
app.config['DESCR'] = "A blueprint to design Python API using Flask-RESTX"
app.config['RESTX_MASK_SWAGGER'] = False

# config (e.g.: mysql)
from .core.configs import getAppConfig
appcfg = getAppConfig()

app.config['MYSQL_DATABASE_USER'] = appcfg['DB']['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = appcfg['DB']['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = appcfg['DB']['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST'] = appcfg['DB']['MYSQL_DATABASE_HOST']
app.config['MYSQL_DATABASE_PORT'] = int(appcfg['DB']['MYSQL_DATABASE_PORT'])


logging.info(app.config)

import app.core.database
import app.apis
