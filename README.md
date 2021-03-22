# notes-selenium
Код, написанный в ходе прохождения курса "Автоматизация тестирования с помощью Selenium и Python" (https://stepik.org/course/575)  
![stepik conquering](https://media.tenor.com/images/ca4da758cdd8816f0e79f5dd0fe83f6d/tenor.gif)  
Заметки:  
* Примеры селекторов:  
  * p[data-type="description"]
    * элемент p с аттрибутом data-type="description"
  * p.text
    * элемент p, класс text
  * .watermelon p.description
  * .banana p
  * //div[@class="row"]/div[2]
  * //img[@id='bullet']
  * //p[contains(text(), "cat")]
  * //img[@name='bullet-cat' and @data-type='animal']
  * [xpath w3](https://www.w3schools.com/xml/xpath_syntax.asp)
  * [xpath MSDN](https://docs.microsoft.com/ru-ru/previous-versions/ms256086(v=vs.120)?redirectedfrom=MSDN)
  * [csss Mozilla](https://developer.mozilla.org/ru/docs/Web/CSS/CSS_Selectors)
  * [csss w3](https://www.w3schools.com/cssref/css_selectors.asp)
* browser.switch_to.window(window_name)
* new_window = browser.window_handles[1]
* Ожидания  
  * browser.implicitly_wait(5)
  * from selenium.webdriver.support.ui import WebDriverWait
  * from selenium.webdriver.support import expected_conditions as EC
  * button = WebDriverWait(browser,5).until(EC.element_to_be_clickable((how,what)))
* pytest hates dots within file names.
* useful pytest commands: https://gist.github.com/amatellanes/12136508b816469678c2
* @pytest.mark.smoke
* @pytest.fixture(scope="function")
* @pytest.fixture(autouse=True)
* pytest -s -v -m smoke test_fixture8.py
* pytest -s -v -m "not smoke" test_fixture8.py
* pytest -s -v -m "smoke or regression" test_fixture8.py
* @pytest.mark.skip
* @pytest.mark.xfail
* pytest -rx -v test_fixture10a.py
  * pytest.mark.xfail(reason="The reason the test should fail is 42")
  * -"rx" to include reason into test report
* @pytest.mark.xfail(reason="fixing this bug right now")
* pytest -rX -v test_fixture10b.py
* https://docs.pytest.org/en/latest/skipping.html Skip and xfail: dealing with tests that cannot succeed.
* https://docs.pytest.org/en/latest/reference/reference.html?highlight=xfail#pytest.mark.xfail
* pytest.ini
  * [pytest]
  * markers =
    * marker1: marker description
* @pytest.mark.parametrize('language', ["ru", "en-gb"])
  * def test_guest_should_see_login_link(browser, language):
  * (NOTE THE QUOTES' USAGE)
* https://docs.pytest.org/en/latest/parametrize.html Parametrizing fixtures and test functions
* conftest.py (to store fixtures; )
  * additional conftest.py files in subdirs are applied to tests in those subdirs.
  * multiple conftest.py files may cause conflicts.
* [Override a fixture on a folder (conftest) level](https://docs.pytest.org/en/latest/fixture.html?highlight=conftest#override-a-fixture-on-a-folder-conftest-level)
* pytest -s -v --browser_name=firefox test_cmd.py
* [addoption](https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption)
* [conftest with browser selection example](https://github.com/cocolacre/notes-selenium/tree/main/3-6_6)
* parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
* pytest -s -v --browser_name=firefox test_parser.py
* pytest-rerunfailures
  * "--reruns n" (rerun failed tests via pytest)
  * **!!! WARNING !!! This module freezes pytest. Investigation needed.**
* "--tb=line" (to shorten test reports)
* фикстура setup
* [PyTest traceback formatting](https://docs.pytest.org/en/latest/usage.html#modifying-python-traceback-printing)
* [Установка языка в Chrome и Firefox для заголовков запросов](https://stepik.org/lesson/237240/step/8)
* [Setting language:](https://github.com/cocolacre/notes-selenium/tree/main/3-6_8)
  * Chrome:
    * from selenium.webdriver.chrome.options import Options
    * options = Options()
    * options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
	* browser = webdriver.Chrome(options=options)
  * Firefox:
    * fp = webdriver.FirefoxProfile()
    * fp.set_preference("intl.accept_languages", user_language)
    * browser = webdriver.Firefox(firefox_profile=fp)
* [Полезные ссылки по PyTest](https://stepik.org/lesson/237258/step/1?unit=209646)
* [Отдельный репозиторий к 4му модулю "Page Object Model"](https://github.com/cocolacre/selenium-autotesting-stepik-4-task-repo)
* [TODO: доделать xfail к багованому товару 4.3-8](https://stepik.org/lesson/201964/step/4?unit=176022)
* [Фреймворки для POM и расширения selenium](https://stepik.org/lesson/213670/step/2?unit=186864)
* [Полезные ссылки 4го модуля: POM, Code Style, Фреймворки](https://stepik.org/lesson/239062/step/1?unit=211485)
* Selenium Grid, Selenoid - для запуска тестов удаленно.
* pytest-html, Allure - отчёты по автотестам.
* pytest-splinter - для скриншотов