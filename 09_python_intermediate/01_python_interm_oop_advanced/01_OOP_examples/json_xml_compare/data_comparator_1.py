from data_readers import ReadXML, ReadJSON


"""Solution 1, classes only for data readers"""

xml_file_path = "OOP_examples/json_xml_compare/example1.xml"
json_file_path = "OOP_examples/json_xml_compare/example1.json"

xml_reader = ReadXML(xml_file_path)
xml_reader.load_xml()
value_xml_1 = xml_reader.get_value("root.item.name")

json_reader = ReadJSON(json_file_path)
json_reader.load_json()
value_json_1 = json_reader.get_value("root.item[0].name")

print(value_xml_1, value_json_1)
assert value_xml_1 == value_json_1
