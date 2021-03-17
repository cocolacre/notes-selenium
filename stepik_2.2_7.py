import os,time,random
from selenium import webdriver
print("os.path.abspath(os.path.dirname(__file__): ", os.path.abspath(os.path.dirname(__file__)))
print("os.path.abspath(__file__): ",os.path.abspath(__file__))
current_dir = os.path.abspath(os.path.dirname(__file__))
fname = "file.txt"
fpath = os.path.join(current_dir, fname)
with open(fpath,"w+") as f:
    f.write("Hello")
#type="file"

url = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    random_string = "ABCDEF0123456789"
    required_fields = browser.find_elements_by_css_selector("input:required[type='text']")
    for field in required_fields:
        input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
        field.send_keys(input_data)
    time.sleep(1)
    browser.find_element_by_css_selector('input[type="file"]').send_keys(fpath)
    browser.find_element_by_css_selector('.btn-primary').click()
except Exception as _e:
    print(str(_e))
finally:
    time.sleep(10)
    browser.quit()