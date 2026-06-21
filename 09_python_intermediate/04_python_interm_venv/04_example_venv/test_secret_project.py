from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *

def test_title_jit():
    driver = webdriver.Safari()
    driver.get("https://jit.team/")
    site_title = driver.title
    print(site_title)
    assert site_title == "Jit Team - IT services & outsourcing company"
    sleep(5)
    driver.quit()

def test_search_google():
    driver = webdriver.Safari()
    driver.get("https://google.com")
    print(driver.title)
    driver.implicitly_wait(3)
    accept_all = driver.find_element(By.ID, "L2AGLb")
    accept_all.click()

    driver.implicitly_wait(3)
    search = driver.find_element(By.ID, "APjFqb")
    search.send_keys("Jit Team")

    driver.implicitly_wait(3)
    search.send_keys(Keys.RETURN)

    sleep(4)

    results = driver.find_element(By.ID, "result-stats")
    print(results.text)

    assert results.text is not None
    driver.quit()
