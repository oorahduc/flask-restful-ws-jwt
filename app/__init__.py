from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restplus import Api
from flask import Blueprint

from .main.config import config_by_name
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask-Restplus-JWT',
          version='1.0',
          description='a boilerplate for a flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)

