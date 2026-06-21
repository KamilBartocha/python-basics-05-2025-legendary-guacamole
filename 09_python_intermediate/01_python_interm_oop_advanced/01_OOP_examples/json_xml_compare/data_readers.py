import xml.etree.ElementTree as ET
import json

class ReadXML:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.root = None

    def load_xml(self):
        try:
            # Parse the XML file
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
        # Split the path into parts
        parts = path.split(".")
        current_elem = self.root

        # Traverse through the XML structure based on the path
        for part in parts:
            if part.startswith("root"):
                continue  # Skip the "root" part of the path
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



class ReadJSON:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_json(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
            print("JSON file loaded successfully.")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _get_element_by_path(self, path):
        parts = path.split(".")
        current_elem = self.data

        for part in parts:
            if '[' in part and ']' in part:
                # Handle list indices like "item[0]"
                key = part[:part.index('[')]  # Get the key part (e.g., "item")
                index = int(part[part.index('[') + 1:part.index(']')])  # Get the index part (e.g., "0")
                current_elem = current_elem.get(key, None)  # Get the list by key
                if current_elem is not None and isinstance(current_elem, list):
                    current_elem = current_elem[index]  # Access the specific index in the list
                else:
                    return None
            else:
                # Handle regular dictionary keys
                current_elem = current_elem.get(part, None)

            if current_elem is None:
                return None
        return current_elem

    def get_value(self, path):
        elem = self._get_element_by_path(path)
        if elem is not None:
            return elem
        else:
            return "Key not found"
