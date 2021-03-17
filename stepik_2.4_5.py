from selenium import webdriver

browser = webdriver.Chrome()
url = "http://suninjuly.github.io/cats.html"
browser.get("url")

button = browser.find_element_by_id("button")