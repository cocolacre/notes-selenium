#XPath notes

xpath1 = "/html/body/header"
xpath2 = "//header"
xpath3 = '//div[@class="col-sm-4"][3]//img' #lenin cat
xpath4 = '//p[text()="Lenin cat"]'
xpath5 = """//p[contains(text(), 'cat')]"""
xpath6 = """//*[contains(@class, "lenin")]"""
xpath7  = """//*[contains(@class, "cat") and contains(@name, "Vova")]"""
xpath8 = "//img[@name='bullet-cat' and @data-type='animal']"

xpath_info = """https://www.w3schools.com/xml/xpath_syntax.asp"""
