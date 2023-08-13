from src.api.services.calendar_service import fetch_events


def test_fetch_events():
    events = fetch_events()
    assert isinstance(events, list)
