from src.api.services.notion_service import fetch_todos, complete_todo


def test_fetch_todos():
    todos = fetch_todos()
    assert isinstance(todos, list)


def test_complete_todo():
    success = complete_todo('test_id')
    assert success == True
