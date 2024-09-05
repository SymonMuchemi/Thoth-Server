from flask import Flask
from flask.ext.sqalchemy import SQLAlchemy
from config import env_config


db = SQLAlchemy()


def create_app(config:str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(env_config[config])
    env_config[config].init_app(app)
    
    db.init_app(app)

    return app
