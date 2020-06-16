from app import app, APPNAME
from flask_restx import Api

from .namespace_root import api as rootNS
# import other namespaces

api = Api(
    title=APPNAME,
    version=app.config['VERSION'],
    description=app.config['DESCR'],
)

BASEPATH = '/{}'.format(app.config['VERSION'])

# add all namespaces
api.add_namespace(rootNS, path=BASEPATH)
# api.add_namespace(otherNS, path=BASEPATH + '/otherNS')

api.init_app(app)
