import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

#answer = math.log(int(time.time()))

def answer():
    return str(math.log(int(time.time())))

url_list = ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"]

#ember95
#.ember-text-area
#.submit-submission
#@pytest.mark.parametrize('urls',url_list)
#.smart-hints__hint
#url = url_list[0]

@pytest.fixture(scope="class")
def browser():
    print("Starting Chrome")
    browser = webdriver.Chrome()
    yield browser
    print("Closing Chrome")
    browser.quit()

@pytest.mark.parametrize('url',url_list)
class TestAliens():
    def test_aliens(self, browser, url):
        browser.get(url)
        #textarea = browser.find_element_by_class_name("ember-text-area")
        textarea = WebDriverWait(browser,10).until(ec.presence_of_element_located((By.CLASS_NAME,"ember-text-area")))
        textarea.send_keys(answer())
        browser.find_element_by_class_name("submit-submission").click()
        hint = WebDriverWait(browser,10).until(ec.presence_of_element_located((By.CLASS_NAME,"smart-hints__hint")))
        hint_text = hint.text
        if not "Correct!" in hint_text:
            with open("alien_messages.txt","a+") as fout:
                fout.write(hint_text + "\n")
        assert "Correct!" in hint_text, f"Got '{hint_text}' instead of 'Correct!'"
