from selenium import webdriver
import openpyxl
import requests
import unittest
import props

# stylesheet col names schema: url | title | description

class LandingPagesMetadataTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://magentofinal.mytriorings.com/'
        wb = openpyxl.load_workbook('metadata.xlsx', data_only=True)
        self.test_data = wb['test_meta']
        self.browser = webdriver.Chrome(props.chrome_path)

    def test_page_metadata(self):
        for data_set in self.test_data:
            url = self.base_url + data_set[0].value
            self.browser.get(url)
            page_description = self.browser.find_element_by_xpath("//meta[@name='description']").get_attribute("content")
            page_title = self.browser.title
            print("[ {} ] | {}".format(page_title, data_set[0].value))
            self.assertEqual(data_set[2].value, page_description)


    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
