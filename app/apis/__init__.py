from app import App, APPNAME
from flask_restx import Api

from .namespace_root import api as rootNS
# import other namespaces

api = Api(
    title=APPNAME,
    version=App.config['VERSION'],
    description=App.config['DESCR'],
)

BASEPATH = '/{}'.format(App.config['VERSION'])

# add all namespaces
api.add_namespace(rootNS, path=BASEPATH)
# api.add_namespace(otherNS, path=BASEPATH + '/otherNS')

api.init_app(App)
