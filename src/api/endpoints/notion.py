from flask import Blueprint, jsonify

notion_blueprint = Blueprint('notion', __name__)


@notion_blueprint.route('/todos', methods=['GET'])
def get_todos():
    # Logic to fetch to-dos from Notion
    return jsonify(todos=[])


@notion_blueprint.route('/todos/complete/<string:todo_id>', methods=['POST'])
def complete_todo(todo_id):
    # Logic to mark a to-do as complete
    return jsonify(success=True)
