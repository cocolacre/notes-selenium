import os, time, random, math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element_by_class_name("btn-primary").click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_class_name("btn-primary").click()
    
    time.sleep(1)
    res = browser.switch_to.alert.text.split(": ")[-1].strip()
    os.system("echo %s | clip"%res)
except Exception as _e:
    print(str(_e))
finally:
    time.sleep(10)
    browser.quit()
#
