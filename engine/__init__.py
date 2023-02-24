from flask import Flask
from public import public

def create_app():
    app = Flask(__name__)

    # blueprints register here
    app.register_blueprint(public, url_prefix='/portfolio')

    return app