from services.weather_service import fetch_current_weather


def test_fetch_current_weather():
    weather_data = fetch_current_weather('New York')
    assert isinstance(weather_data, dict)
