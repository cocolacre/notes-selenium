# notes-selenium
Код, написанный в ходе прохождения курса "Автоматизация тестирования с помощью Selenium и Python" (https://stepik.org/course/575)

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
* [PyTest traceback formatting](https://docs.pytest.org/en/latest/usage.html#modifying-python-traceback-printing)


