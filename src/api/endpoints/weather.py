from flask import Blueprint, jsonify

weather_blueprint = Blueprint('weather', __name__)


@weather_blueprint.route('/current/<string:location>', methods=['GET'])
def get_current_weather(location):
    # Logic to fetch current weather for the given location
    return jsonify(weather={})
