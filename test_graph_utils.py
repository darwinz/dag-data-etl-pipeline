import json
from unittest import TestCase

from graph_utils import GraphUtils


class TestGraphUtils(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_graph(self):
        with open('data.json') as fixture:
            dict_list = json.load(fixture)
            graph = GraphUtils.create_graph(dict_list[0])
            self.assertIn("Monkey", graph)
            self.assertEqual(graph['Animal']['children'], ["Monkey"])
