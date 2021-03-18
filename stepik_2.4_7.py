from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import time

#browser.implicitly_wait(5)


# EXPLICIT WAITS:
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait2.html")
    button = WebDriverWait(browser,5).until(ec.element_to_be_clickable((By.ID, "verify")))
    button.click()
    msg = browser.find_element_by_id("verify_message")
    assert "successful" in msg.text
    
except Exception as _e:
    print(str(_e))
    
finally:
    time.sleep(10)
    browser.quit()


infos = """

NoAlertPresentException
NoSuchElementException
NoSuchFrameException
StaleElementReferenceException
WebDriverException
WebElement
_element_if_visible
_find_element
_find_elements
alert_is_present
element_located_selection_state_to_be
element_located_to_be_selected
element_selection_state_to_be
element_to_be_clickable
element_to_be_selected
frame_to_be_available_and_switch_to_it
invisibility_of_element
invisibility_of_element_located
new_window_is_opened
number_of_windows_to_be
presence_of_all_elements_located
presence_of_element_located
staleness_of
text_to_be_present_in_element
text_to_be_present_in_element_value
title_contains
title_is
url_changes
url_contains
url_matches
url_to_be
visibility_of
visibility_of_all_elements_located
visibility_of_any_elements_located
visibility_of_element_located
"""