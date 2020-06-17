import logging
from app import App
import pymysql.cursors

# https://github.com/cyberdelia/flask-mysql
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(App)


def connect(cursor_type=pymysql.cursors.DictCursor):
    logging.info('Connecting to db...')
    conn = mysql.connect()
    logging.info('Successfully connected to db')
    return conn, mysql.get_db().cursor(cursor_type)

# def query(query, params):
#     error = None
#     try:
#         conn, cur = connect()
#         logging.info('Successfully connected to db')

#         cur.execute(query, params)
#         logging.info('Query <<{}>> done on db'.format(query))
        
#     except Exception as ex:
#         logging.error(ex)
#         error = ({ 'error': str(ex) }, 500)
#     finally:
#         conn.close()
#         return error