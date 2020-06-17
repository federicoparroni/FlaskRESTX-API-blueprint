from flask import request
from flask_restx import Namespace, Resource
from app.core.database import connect
from app import App
import logging

api = Namespace('Status', description='General info')

# from .model import UserModel

@App.before_request
def before_request_func():
    logging.info('Request received')

@App.after_request
def after_request_func(response):
    logging.info('Request completed')
    return response
# ==========

@api.route('/')
class Status(Resource):
    def get(self):
        return {'status': 'OK'}

# userPOST_parser = api.parser()
# userPOST_parser.add_argument('iduser', type=int, required=True,
#                             location='form', help="User id")
# userPOST_parser.add_argument('username', type=str, required=True,
#                             location='form', help="Username")
#
# @api.route('/user/<string:username>')
# class UserList(Resource):

#     # get a user
#     @api.marshal_list_with(UserModel)
#     def get(self, username):
#         QUERY = 'SELECT * FROM Users WHERE username = %s'
#         PARAMS = (username)
#         try:
#             conn, cur = connect()
#             cur.execute(QUERY, PARAMS)
#             users = cur.fetchall()
#             return { 'users': users }, 206
#         except Exception as ex:
#             logging.error(ex)
#             return {}, 500
#         finally:
#             cur.close()
#             conn.close()
