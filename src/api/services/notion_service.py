import dataclasses
from typing import Dict

from notion_client import Client

from config import NOTION_API_TOKEN, NOTION_DATABASE_ID


@dataclasses.dataclass(frozen=True)
class Task:
    """ A to-do item from Notion """
    id: str
    label: str
    is_done: bool
    motivation_cost: int

    @staticmethod
    def load_from_notion(todo_dict: dict):
        return Task(
            id=todo_dict['id'],
            label=todo_dict['properties']['Name']['title'][0]['plain_text'],
            is_done=todo_dict['properties']['Status']['select']['name'] in ['Done', 'Canceled'],
            motivation_cost=todo_dict['properties']['Motivation cost']['number']
        )


def fetch_today_tasks() -> list[Task]:
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

    return tasks


def fetch_tasks_count() -> Dict[str, int]:
    """
    Fetch statistics about all tasks from a Notion database.
    :return: A dict of integers with three keys: 'nb_done', 'nb_pending' and 'motivation_cost_sum'.
    """
    notion = Client(auth=NOTION_API_TOKEN)

    has_more = True
    cursor = None
    nb_done = 0
    nb_pending = 0
    motivation_cost_sum = 0

    # Fetch tasks count from Notion
    # Since the API doesn't provide a count method, we have to fetch all tasks and count them
    while has_more:
        answer = notion.databases.query(
            database_id=NOTION_DATABASE_ID,
            filter={
                "or": [
                    {"property": "Status", "select": {"equals": "Done"}},
                    {"property": "Status", "select": {"equals": "Pending"}},
                    {"property": "Status", "select": {"equals": "In Progress"}},
                ]
            },
            filter_properties=['Name', 'Status', 'Motivation cost'],
            page_size=100,
            start_cursor=cursor,
        )

        # Track pagination
        cursor = answer.get("next_cursor")
        has_more = answer.get("has_more")

        # Convert the list of dicts to a list of task objects
        tasks_batch = [Task.load_from_notion(task) for task in answer.get("results")]

        # Count tasks
        nb_done_batch = sum(1 for task in tasks_batch if task.is_done)
        nb_done += nb_done_batch
        nb_pending += len(tasks_batch) - nb_done_batch
        motivation_cost_sum += sum(task.motivation_cost for task in tasks_batch
                                   if task.motivation_cost is not None and task.is_done)

    return {'nb_done': nb_done, 'nb_pending': nb_pending, 'motivation_cost_sum': motivation_cost_sum}


def complete_task(task_id: str) -> bool:
    """
    Mark a task as completed in Notion by changing its status to "Done".

    :param task_id: The ID of the task to complete.
    :return: True if the task was successfully marked as completed, False otherwise.
    """
    notion = Client(auth=NOTION_API_TOKEN)

    # Update the task status
    task = notion.pages.update(
        page_id=task_id,
        properties={
            "Status": {"select": {"name": "Done"}}
        }
    )

    task = Task.load_from_notion(task)
    return task.is_done
