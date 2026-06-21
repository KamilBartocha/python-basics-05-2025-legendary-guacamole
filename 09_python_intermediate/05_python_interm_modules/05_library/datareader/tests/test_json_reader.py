import unittest
import logging
import sys
from datareader.json_reader import ReadJSON

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stdout))

class TestReadJSON(unittest.TestCase):
    def test_load_json(self):
        reader = ReadJSON('example1.json')
        reader.load_json()
        self.assertIsNotNone(reader.data)

    def test_get_value(self):
        reader = ReadJSON('example1.json')
        reader.load_json()
        value = reader.get_value('root.item[0].name')
        # logging.getLogger().info(value)
        self.assertEqual(value, 'Item 1')

if __name__ == "__main__":
    unittest.main()
