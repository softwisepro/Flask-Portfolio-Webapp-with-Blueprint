from flask import Flask, redirect, url_for
from public import public

def create_app():
    app = Flask(__name__)

    # blueprints register here
    app.register_blueprint(public, url_prefix='/portfolio')

    @app.route('/')
    def index():
        return redirect(url_for('public.index'))

    return app