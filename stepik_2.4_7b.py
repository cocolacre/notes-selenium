from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def scroll_to(driver, element):
    js = "return arguments[0].scrollIntoView(true);"
    driver.execute_script(js, element)
    
#browser.implicitly_wait(5)


# EXPLICIT WAITS:
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    WebDriverWait(browser,10).until(ec.text_to_be_present_in_element((By.ID,"price"), "$100"))
    print("Clicking")
    browser.find_element_by_id("book").click()
    
    js = "return arguments[0].scrollIntoView(true);"
    x = browser.find_element_by_id("input_value")
    browser.execute_script(js, x)
    
    y = calc(x.text)
    input_field = browser.find_element_by_id("answer")
    scroll_to(browser, input_field)
    input_field.send_keys(y)
    
    scroll_to(browser, browser.find_element_by_id("solve"))
    browser.find_element_by_id("solve").click()
    
    #button = WebDriverWait(browser,5).until(ec.element_to_be_clickable((By.ID, "verify")))
    #button.click()
    #msg = browser.find_element_by_id("verify_message")
    #assert "successful" in msg.text
    
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