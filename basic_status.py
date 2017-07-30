import requests
import os
from selenium import webdriver

# root_path = os.path.dirname(__file__)
r = requests.get('http://magentofinal.mytriorings.com/some_page')
print(r.status_code)

# print(os.path.join(root_path, 'browser', 'chromedriver.exe'))
# chromedriver_path = os.path.join(root_path, 'browser', 'chromedriver.exe')
# print(chromedriver_path)
# cr_path = 'https://sites.google.com/a/chromium.org/chromedriver/home'

browser = webdriver.Chrome(r'C:\bin\selenium\chromedriver230.exe')
browser.maximize_window()
browser.get('http://mytriorings.com')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.save_screenshot('shot.png')
browser.get_screenshot_as_file('as_file.png')
print(browser.title)
browser.quit()

class HttpStatusCodesTest(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
