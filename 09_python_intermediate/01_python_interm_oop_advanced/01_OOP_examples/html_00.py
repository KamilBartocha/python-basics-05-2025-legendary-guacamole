from bs4 import BeautifulSoup


html_content = '''
<html>
<head><title>Test Page</title></head>
<body>
    <h1>Welcome to My Test Page</h1>
    <p class="description">This is a sample paragraph.</p>
    <a href="http://example.com">Example Link</a>
    <meta property="twitter:description" content="The primary skill of ours - coding! We specialize in most of the currently considered to be standard technologies, but we are always open for the undiscovered ones! Our employees have been part of many innovative projects that included cutting-edge technologies.">
</body>
</html>
'''

soup = BeautifulSoup(html_content, 'html.parser')
# html.parser - brak instalacji dodatkowych bibliotek, domyslny w pythonie
# lxml - szybszy i zgodny z xml ale wymaga instalacji lxml
# html5lib - zgodny z html5

title = soup.title.string
print(f"Title: {title}")

# Find and print the first paragraph with class 'description'
paragraph = soup.find('p', class_='description').text
print(f"Paragraph: {paragraph}")

meta_tag = soup.find('meta', attrs={'property': 'twitter:description'})
meta_content = meta_tag['content'] if meta_tag else 'Meta tag not found'
print(f"meta_content: {meta_content}")


# Find and print the href attribute of the first link
link = soup.find('a')['href']
print(f"Link: {link}")
