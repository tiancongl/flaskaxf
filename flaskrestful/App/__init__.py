from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_api


def create_app():
     app = Flask(__name__)

     app.config.from_object(envs.get("develop"))

     init_ext(app)

     init_api(app)


     return app