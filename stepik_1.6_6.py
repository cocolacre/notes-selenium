from selenium import webdriver
import time , random

random_string = "abcdefghijklmnopqrstuvwxyz"


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    time.sleep(1)
    elements = browser.find_elements_by_tag_name("input")
    
    for element in elements:
       input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
       element.send_keys(input_data)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла