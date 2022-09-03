from flask import Flask, render_template
from flask_cors import CORS
from flask_login import LoginManager
from app.config import Config, DevelopmentConfig, ProductionConfig, TestingConfig
import logging

from app.auth.controllers import auth as auth
from app.api.controllers import api as api
from app.client.controllers import frontend as frontend
from app.settings import db, migrate, create_folder
from app.auth.models import User

CONFIG_ORIGINS = [
    'http://localhost:8080',  # React
    'http://127.0.0.1:8080',  # React
  ]


logging.basicConfig(filename='app/logs/app.log',encoding='utf-8', level=logging.INFO)
logging.getLogger("werkzeug").setLevel(logging.WARNING)

app = Flask(__name__, static_folder = 'frontend/build', static_url_path = '')
cors = CORS(app, resources={r"/api": {"origins": CONFIG_ORIGINS}})
app.config.from_object(DevelopmentConfig)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

db.init_app(app)
db.app = app
db.create_all()
migrate.init_app(app, db,render_as_batch=True)

create_folder(app.config['DATA_FOLDER'])

login_manager = LoginManager()
login_manager.login_view = 'auth.signin'
login_manager.init_app(app)


app.register_blueprint(auth)
app.register_blueprint(api)
app.register_blueprint(frontend)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))