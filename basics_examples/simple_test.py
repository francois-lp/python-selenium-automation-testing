import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(
            executable_path='F:\Drivers\mozilla-geckodriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver

        # open a new browser and go to python.org
        driver.get('http://www.python.org')

        # check if title has 'Python' word in it
        self.assertIn('Python', driver.title)

        # do a research
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)

        # ensure that some results are found
        assert 'No results found.' not in driver.page_source

    def tearDown(self):
        pass
        # self.driver.close()


if __name__ == '__main__':
    unittest.main()
