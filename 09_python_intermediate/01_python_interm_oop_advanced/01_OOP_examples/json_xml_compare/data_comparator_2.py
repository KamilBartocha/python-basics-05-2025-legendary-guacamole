from data_readers import ReadXML, ReadJSON

class FileReader:
    def __init__(self, xml_file_path, json_file_path):
        self.xml_reader = ReadXML(xml_file_path)
        self.json_reader = ReadJSON(json_file_path)

    def load_files(self):
        """Load both the XML and JSON files."""
        self.xml_reader.load_xml()
        self.json_reader.load_json()

    def get_xml_value(self, path):
        """Get a specific value from the XML file based on the path."""
        return self.xml_reader.get_value(path)

    def get_json_value(self, path):
        """Get a specific value from the JSON file based on the path."""
        return self.json_reader.get_value(path)

    def compare_values(self, xml_path, json_path):
        """Compare values from both XML and JSON files at specified paths."""
        xml_value = self.get_xml_value(xml_path)
        json_value = self.get_json_value(json_path)

        if xml_value == json_value:
            print(f"Match found: {xml_value}={json_value}")
        else:
            print(f"No Match: XML -> {xml_value} | JSON -> {json_value}")


"""Solution 2 Class for comparing"""
xml_file_path = "OOP_examples/json_xml_compare/example1.xml"
json_file_path = "OOP_examples/json_xml_compare/example1.json"

# Create an instance of the FileReader class
file_reader = FileReader(xml_file_path, json_file_path)

file_reader.load_files()

# Get specific values from XML and JSON
val_xml = file_reader.get_xml_value("root.item.name")
val_json = file_reader.get_json_value("root.item[0].name")

file_reader.compare_values("root.item.name", "root.item[0].name")
