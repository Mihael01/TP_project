
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    @app.route('/')
    def hello_world():
        return 'Welcome to "Student marks" app!'

    bootstrap = Bootstrap(app)
    migrate = Migrate(app, db)    
    from app import models

    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
        
    return app


