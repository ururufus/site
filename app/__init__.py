from flask import Flask
from .extensions import db
from .config import Config

from .routes.user import user
from .routes.post import post
from .routes.main import main
from .routes.post_song import post_song
from .routes.post_menu import post_menu



def create_app(config_class=Config):
    app = Flask(__name__)

    #app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    #app.config['SECRET_KEY'] = 'hbvgfcdxhjknkm897654jhklm54609@@@@q'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #всё что выше переехало с помощью конфиг файла в одну строчку ниже
    app.config.from_object(config_class)

    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(main)
    app.register_blueprint(post_song)
    app.register_blueprint(post_menu)

    db.init_app(app) # Позднее связывание с bd без использования здесь db = SQLAlchemy(app) - хотим разнести контексты

    with app.app_context():
        db.create_all()

    return app