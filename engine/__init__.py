from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='portfolio',
    )

    # import blueprint
    from public import public
    from .views import engine

    # blueprints register here
    app.register_blueprint(engine, url_prefix='/')
    app.register_blueprint(public, url_prefix='/portfolio')

    return app