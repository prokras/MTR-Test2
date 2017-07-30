import requests
import unittest
import props

# Test status Codes of ulrs

class HttpStatusCodesTest(unittest.TestCase):

    def setUp(self):
        # open file with ulrs
        self.base_url = 'http://magentofinal.mytriorings.com/'
        self.paths = props.url_for_test
        self.broken_paths = []

    def test(self):
        error_msg = ""
        has_broken_urls = False
        for path in self.paths:
            url = self.base_url + path
            r = requests.get(url)
            try:
                self.assertEqual(200, r.status_code)
            except AssertionError as e:
                error_msg = " -- ERR-- {}".format(e)
                has_broken_urls = True
                self.broken_paths.append(path)
            print("{} - {}{}".format(r.status_code, path, error_msg))
        self.assertFalse(has_broken_urls)

    def tearDown(self):
        print("tear down")
        for broken_path in self.broken_paths:
            print(broken_path)

if __name__ == '__main__':
    unittest.main()
