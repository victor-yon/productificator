import unittest

from services.notion_service import fetch_today_tasks, complete_task, fetch_tasks_count


class MyTestCase(unittest.TestCase):

    def test_set_token(self):
        from config import NOTION_API_TOKEN
        self.assertIsNotNone(NOTION_API_TOKEN)
        self.assertTrue(len(NOTION_API_TOKEN) > 0)
        self.assertTrue(NOTION_API_TOKEN.startswith('secret_'))

    def test_fetch_today_tasks(self):
        todos = fetch_today_tasks()
        self.assertIsInstance(todos, list)

    def test_fetch_tasks_count(self):
        counts = fetch_tasks_count()
        self.assertIsInstance(counts, dict)
        self.assertIn('nb_done', counts)
        self.assertIn('nb_pending', counts)
        self.assertIn('motivation_cost_sum', counts)
        self.assertGreater(counts['nb_done'], 1)
        self.assertGreater(counts['nb_pending'], 1)
        self.assertGreater(counts['motivation_cost_sum'], 1)

    def test_complete_todo(self):
        # TODO: find a way to test this method without hard-coding a task ID
        success = complete_task('05352f43a9c1417c93c33e5252855468')
        self.assertIs(success, True)
