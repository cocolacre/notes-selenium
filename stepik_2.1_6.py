from selenium import webdriver
import math, os,time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    selector1 = ".form-group label span:nth-child(1)"
    
    x = browser.find_element_by_css_selector("#treasure").get_attribute("valuex")
    y = calc(x)
    selector4 = "#robotCheckbox"
    selector5 = "#robotsRule"
    selector6 = ".btn-default"
    
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector(selector4).click()
    browser.find_element_by_css_selector(selector5).click()
    browser.find_element_by_css_selector(selector6).click()
    
    
except Exception as _e:
    print(str(_e))
finally:
    time.sleep(10)
    browser.quit()