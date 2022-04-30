import secrets
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

from . import blueprints


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    Bootstrap(app)

    app.config['SECRET_KEY'] = secrets.token_hex(64)

    if not os.path.isdir(app.instance_path):
        os.makedirs(app.instance_path)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(app.instance_path, "data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return blueprints.user.User.query.get(user_id)

    for module_ in dir(blueprints):
        module_obj = getattr(blueprints, module_)
        if hasattr(module_obj, 'bp'):
            app.register_blueprint(getattr(module_obj, 'bp'))

    db.init_app(app)
    Migrate(app, db)

    return app
