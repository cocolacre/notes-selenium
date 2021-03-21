import pytest
import time

class TestAddToCartButton():
    def test_add_to_cart_button_exists(self,browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(url)
        time.sleep(30)
        button_found = False
        #проверяем, что найдено больше нуля кнопок .btn-add-to-basket
        button_found = len(browser.find_elements_by_class_name("btn-add-to-basket")) > 0
        #(button_found равно True, если len(find_elements...) больше нуля.)
        # Подробнее тут: https://stepik.org/lesson/237240/step/9?discussion=1191413
        assert button_found, "Не найдена кнопка добавления товара в корзину"
#
