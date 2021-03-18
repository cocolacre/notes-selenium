import unittest
from selenium import webdriver
import time, random

class TestRegistrationForms(unittest.TestCase):

    def test_form_1(self):
        try:
            random_string = "abcdefghijklmnopqrstuvwxyz"
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            
            field1 = browser.find_element_by_css_selector("input.first:required")
            input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
            field1.send_keys(input_data)
            
            field2 = browser.find_element_by_css_selector("input.second:required")
            input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
            field2.send_keys(input_data)
            
            field3 = browser.find_element_by_css_selector("input.third:required")
            input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
            field3.send_keys(input_data)
            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
        
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
        
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            expected_text = "Congratulations! You have successfully registered!"
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(expected_text,welcome_text,"welcome_text does not match expected_text")
        finally:
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_form_2(self):
        try:
            random_string = "abcdefghijklmnopqrstuvwxyz"
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            
            field1 = browser.find_element_by_css_selector("input.first:required")
            input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
            field1.send_keys(input_data)
            
            field2 = browser.find_element_by_css_selector("input.second:required")
            input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
            field2.send_keys(input_data)
            
            field3 = browser.find_element_by_css_selector("input.third:required")
            input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
            field3.send_keys(input_data)
            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
        
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
        
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            expected_text = "Congratulations! You have successfully registered!"
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(expected_text,welcome_text,"welcome_text does not match expected_text")
        finally:
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()



if __name__ == "__main__":
	unittest.main()
	