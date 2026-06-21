import json

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
                key = part[:part.index('[')]
                index = int(part[part.index('[') + 1:part.index(']')])
                current_elem = current_elem.get(key, None)
                if current_elem is not None and isinstance(current_elem, list):
                    current_elem = current_elem[index]
                else:
                    return None
            else:
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
