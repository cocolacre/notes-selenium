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
