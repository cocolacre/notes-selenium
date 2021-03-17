import time
from selenium import webdriver
import math, os,time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
print("test[1]")
try:
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
except Exception as _e:
    print(str(_e))

time.sleep(5)
print("test[2]")
    
try:
    js1 = "return arguments[0].scrollIntoView(true);"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script(js1, button)
    button.click()
except Exception as _e:
    print(str(_e))
time.sleep(5)

print("test[3]")
try:
    browser.get(link)
    js1 = "return arguments[0].scrollIntoView(true);"
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script(js1, button)
    button.click()
except Exception as _e:
    print(str(_e))

time.sleep(5)
browser.quit()