import unittest
from datareader.xml_reader import ReadXML

class TestReadXML(unittest.TestCase):
    def test_load_xml(self):
        reader = ReadXML('example1.xml')
        reader.load_xml()
        self.assertIsNotNone(reader.root)

    def test_get_value(self):
        reader = ReadXML('example1.xml')
        reader.load_xml()
        value = reader.get_value('root.item.name')
        self.assertEqual(value, 'Item 1')

if __name__ == "__main__":
    unittest.main()
