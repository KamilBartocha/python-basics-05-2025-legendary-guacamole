# mydatareader

`mydatareader` is a Python library for reading and processing XML and JSON data.

## Installation

You can install the library using pip:

```bash
pip install mydatareader
```

## Usage
#### Reading XML

```python
from mydatareader import ReadXML

xml_reader = ReadXML('path_to_xml_file.xml')
xml_reader.load_xml()
value = xml_reader.get_value('root.element')
```

#### Reading JSON

```python
from mydatareader import ReadJSON

json_reader = ReadJSON('path_to_json_file.json')
json_reader.load_json()
value = json_reader.get_value('key[0].nestedKey')
```
