from os import environ as env
from dotenv import load_dotenv
import logging

'''
LOGGING CONFIG
'''

logging.basicConfig(level=logging.INFO)

'''
APP CONFIG
'''

load_dotenv()

AUTH0_DOMAIN = env.get('AUTH0_DOMAIN')
ALGORITHMS = env.get('ALGORITHMS')
API_AUDIENCE = env.get('API_AUDIENCE')

AUTH0_CLIENT_ID=env.get('AUTH0_CLIENT_ID')



class Config(object):
    try:
        # heroku calls db starting with URI postgres:// but within psql this has changed to postgresql, so we edit
        # manually
        SQLALCHEMY_DATABASE_URI = env.get('DATABASE_URL').replace("://", "ql://", 1)
    except:
        SQLALCHEMY_DATABASE_URI = env.get('LOCAL_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(object):
    SQLALCHEMY_DATABASE_URI = env.get('LOCAL_TEST_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

