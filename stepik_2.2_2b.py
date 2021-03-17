from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math, os,time
html = """
<label for="dropdown">Выберите язык программирования:</label>
<select id="dropdown" class="custom-select">
 <option selected>--</option>
 <option value="1">Python</option>
 <option value="2">Java</option>
 <option value="3">JavaScript</option>
</select>
"""
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    
    #browser.find_element_by_css_selector("option:nth-child(2)").click()
    #browser.find_element_by_css_selector("[value='1']").click()
    
    select = Select(browser.find_element_by_tag_name("select"))
    
    num = str(int(num1)+int(num2))
    print("num:", num)
    select.select_by_value(num)
    
    #select.select_by_visible_text("text")
    #langs = { "Python" : 1 }
    #select.select_by_index(langs["Python"])
    
    browser.find_element_by_class_name("btn-default").click()
except Exception as _e:
    print(str(_e))
finally:
    time.sleep(10)
    browser.quit()

