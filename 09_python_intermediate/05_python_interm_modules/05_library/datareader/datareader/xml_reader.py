import xml.etree.ElementTree as ET

class ReadXML:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.root = None

    def load_xml(self):
        try:
            self.tree = ET.parse(self.file_path)
            self.root = self.tree.getroot()
            print("XML file loaded successfully.")
        except ET.ParseError as e:
            print(f"Error parsing XML file: {e}")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _get_element_by_path(self, path):
        parts = path.split(".")
        current_elem = self.root

        for part in parts:
            if part.startswith("root"):
                continue
            current_elem = current_elem.find(part)
            if current_elem is None:
                return None
        return current_elem

    def get_value(self, path):
        elem = self._get_element_by_path(path)
        if elem is not None:
            return elem.text
        else:
            return "Key not found"
