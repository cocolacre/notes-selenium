import math, os, time
from selenium import webdriver
try:
    browser = webdriver.Chrome()
    for i in range(5):
        browser.execute_script("document.title='Script executing[%s]';"%str(i+1))
        time.sleep(1)
    browser.execute_script("alert('Robots at work');")
    
except Exception as _e:
    print(str(_e))
finally:
    time.sleep(10)
    browser.quit()