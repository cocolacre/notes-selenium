from selenium import webdriver
import math, os,time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    
    selector1 = ".form-group label span:nth-child(1)"
    selector2 = ".form-group label span:nth-child(2)"
    selector3 = "#input_value"
    x = str(browser.find_element_by_css_selector(selector3).text)
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
    os.system("echo %s | clip"%y)
    time.sleep(10)
    browser.quit()