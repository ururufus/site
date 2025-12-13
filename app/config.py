import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'postgres')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'password')
    HOST = os.environ.get('POSTGRES_HOST', 'postgres')
    PORT = os.environ.get('POSTGRES_PORT', '5432')
    DB = os.environ.get('POSTGRES_DB', 'test_name')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = 'hbvgfcdxhjknkm897654jhklm54609@@@@q'
    SQLALCHEMY_TRACK_MODIFICATIONS = True