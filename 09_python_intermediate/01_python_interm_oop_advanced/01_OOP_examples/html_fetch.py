# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup


class HTMLProcessor:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def load_html(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.text, 'html.parser')
                print("HTML content loaded successfully.")
            else:
                print(f"Failed to retrieve page. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def extract_elements(self, tag, class_name=None):
        if self.soup:
            if class_name:
                elements = self.soup.find_all(tag, class_=class_name)
            else:
                elements = self.soup.find_all(tag)
            return [element.find('p', class_='AboutPeople__name').text for element in elements]
            # return [element.text.strip() for element in elements]
        else:
            print("HTML content is not loaded yet.")
            return []


url = 'https://jit.team/about'
processor = HTMLProcessor(url)
processor.load_html()


names = processor.extract_elements('div', class_name='AboutPeople__person')  # Assuming 'div' with class 'AboutPeople__person' contains the data
for name in names:
    print(name)
