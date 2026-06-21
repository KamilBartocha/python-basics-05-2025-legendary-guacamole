from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Ustawienie ścieżki do ChromeDriver
# driver = webdriver.Chrome()
driver = webdriver.Safari()

try:
    driver.get("https://www.google.com")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    first_result = driver.find_element_by_css_selector("h3")
    first_result.click()

finally:
    driver.quit()
