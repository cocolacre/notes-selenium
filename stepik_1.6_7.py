from selenium import webdriver
import time 

url = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    value1 = "input"
    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    value2 = "last_name"
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    value3 = "city"
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    value4 = "country"
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    #button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла