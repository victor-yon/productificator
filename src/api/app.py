from flask import Flask

from endpoints.calendar import calendar_blueprint
from endpoints.notion import notion_blueprint
from endpoints.weather import weather_blueprint


def create_app():
    app = Flask(__name__)

    # Load configuration if needed
    # app.config.from_object('config')

    # Register blueprints for each API section
    app.register_blueprint(notion_blueprint, url_prefix='/notion')
    app.register_blueprint(weather_blueprint, url_prefix='/weather')
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
