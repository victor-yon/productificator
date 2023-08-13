import unittest

from src.api.services.notion_service import fetch_today_tasks, complete_task


class MyTestCase(unittest.TestCase):

    def test_set_token(self):
        from src.api.config import NOTION_API_TOKEN
        self.assertIsNotNone(NOTION_API_TOKEN)
        self.assertTrue(len(NOTION_API_TOKEN) > 0)
        self.assertTrue(NOTION_API_TOKEN.startswith('secret_'))

    def test_fetch_today_tasks(self):
        todos = fetch_today_tasks()
        self.assertIsInstance(todos, dict)
        self.assertEqual(len(todos), 2)
        self.assertIsInstance(todos['todo'], list)

    def test_complete_todo(self):
        success = complete_task('test_id')
        self.assertIs(success, True)
