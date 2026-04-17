from flask import Flask
from .db import db
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food.db'

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app


def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret'

    jwt = JWTManager(app)