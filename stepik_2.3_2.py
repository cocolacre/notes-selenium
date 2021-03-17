js = """alert("Hello!");"""


alert = browser.switch_to.alert
print(alert.text)
alert.accept()

confirm = browser.switch_to.alert
confirm.accept()
#confirm.dismiss()

prompt = browser.switch_to.alert
prompt.send_keys("cocolacre")
prompt.accept()



