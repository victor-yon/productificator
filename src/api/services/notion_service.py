import dataclasses

from notion_client import Client

from src.api.config import NOTION_API_TOKEN, NOTION_DATABASE_ID


@dataclasses.dataclass(frozen=True)
class Task:
    """ A to-do item from Notion """
    id: str
    name: str
    is_done: bool
    motivation_cost: int

    @staticmethod
    def load_from_notion(todo_dict: dict):
        return Task(
            id=todo_dict['id'],
            name=todo_dict['properties']['Name']['title'][0]['plain_text'],
            is_done=todo_dict['properties']['Status']['select']['name'] in ['Done', 'Wait Validation', 'Canceled'],
            motivation_cost=todo_dict['properties']['Motivation cost']['number']
        )


def fetch_today_tasks() -> dict[str, list[Task]]:
    """
    Fetch tasks from a Notion database, and filter them to only return the ones that have to be done today.
    :return: A dict with two keys: 'todo' and 'done'. Each key contains a list of Task objects.
    """
    notion = Client(auth=NOTION_API_TOKEN)

    # Fetch to-dos from Notion
    # Select only the to-dos that are marked as "Today"
    tasks = notion.databases.query(
        database_id=NOTION_DATABASE_ID,
        filter={"property": "Today", "checkbox": {"equals": True}},
        filter_properties=['Name', 'Status', 'Motivation cost'],
        sorts=[
            {"property": "Priority", "direction": "ascending"},
            {"property": "Date Due", "direction": "ascending"},
            {"property": "Created Time", "direction": "ascending"},
        ]
    ).get("results")

    # Convert the list of dicts to a list of task objects
    tasks = [Task.load_from_notion(task) for task in tasks]
    tasks_todo = [task for task in tasks if not task.is_done]
    tasks_done = [task for task in tasks if task.is_done]

    return {'todo': tasks_todo, 'done': tasks_done}


def complete_task(task_id: str) -> bool:
    # Logic to mark a to-do as complete in Notion
    # You'll need to use the Notion API here with proper authentication
    success = True
    return success
