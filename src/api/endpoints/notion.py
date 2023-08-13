from flask import Blueprint, jsonify

from api.services.notion_service import fetch_today_tasks

notion_blueprint = Blueprint('notion', __name__)


@notion_blueprint.route('/today_tasks', methods=['GET'])
def get_today_tasks():
    # Logic to fetch to-dos from Notion
    return jsonify(fetch_today_tasks())


@notion_blueprint.route('/todos/complete/<string:task_id>', methods=['POST'])
def complete_task(task_id: str):
    # Logic to mark a to-do as complete
    return jsonify(success=True)
