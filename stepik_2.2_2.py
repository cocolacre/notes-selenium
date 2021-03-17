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

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()
browser.find_element_by_css_selector("[value='1']").click()

select = Select(browser.find_element_by_tag_name("select"))

select.select_by_value("1") # ищем элемент с текстом "Python"
select.select_by_visible_text("text")
langs = { "Python" : 1 }
select.select_by_index(langs["Python"])


