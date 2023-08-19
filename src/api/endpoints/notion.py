from flask import Blueprint, jsonify

from services.notion_service import fetch_today_tasks, fetch_tasks_count

notion_blueprint = Blueprint('notion', __name__)


@notion_blueprint.route('/all', methods=['GET'])
def get_all():
    # TODO: perform every request in parallel
    today_tasks = fetch_today_tasks()
    tasks_stats = fetch_tasks_count()

    return jsonify({'today_tasks': today_tasks, 'tasks_stats': tasks_stats})


@notion_blueprint.route('/today_tasks', methods=['GET'])
def get_today_tasks():
    # Logic to fetch tasks from Notion
    return jsonify(fetch_today_tasks())


@notion_blueprint.route('/tasks_stats', methods=['GET'])
def get_tasks_stats():
    # Logic to fetch tasks statistics from Notion
    return jsonify(fetch_tasks_count())


@notion_blueprint.route('/todos/complete/<string:task_id>', methods=['POST'])
def complete_task(task_id: str):
    # Logic to mark a to-do as complete
    return jsonify(success=True)
