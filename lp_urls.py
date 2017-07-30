from selenium import webdriver
import requests
import unittest
import sys
import props

class LandingPagesUrlsTest(unittest.TestCase):

    def isTemporary(self, link_href):
        if link_href.find('#') == len(link_href)-1:
            return True


    def setUp(self):
        self.base_url = "http://magentofinal.mytriorings.com/"
        self.paths = props.url_for_test
        self.browser = webdriver.Chrome(props.chrome_path)

    def test_page_ulrs_status(self):
        status_msg = ""
        has_broken_urls = False
        for path in self.paths:
            url = self.base_url + path
            self.browser.get(url)
            print("\n >>> {}".format(self.browser.title))
            main_container = self.browser.find_element_by_class_name("main-container")
            links = main_container.find_elements_by_tag_name("a")
            for link in links:
                link_text = link.text
                link_href = link.get_attribute("href")
                if link_href.find('@') > 0:
                    print('Email link {}'.format(link_href))
                    continue
                if link_href == '':
                    print('ERROR -- EMPTY href attribute {}'.format(link_text))
                    continue
                http_status = requests.get(link_href).status_code
                try:
                    self.assertEqual(200, http_status)
                    status_msg = "OK"
                    if self.isTemporary(link_href):
                        status_msg = "TEMPORARY"
                except AssertionError as e:
                    status_msg = "ERROR - {}".format(e)
                    has_broken_urls = True
                print("{} - {} | [ {} ] - {}".format(http_status, status_msg, link_text, link_href))
        self.assertFalse(has_broken_urls)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
