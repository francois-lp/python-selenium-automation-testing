from model.tests.abstract_test import AbstractTest
from selenium.webdriver.common.keys import Keys


class ProgrammingResearchTest(AbstractTest):

    CONFIG_BREAK_TIME = 1
    CONFIG_OUTPUT_TEST_DIRECTORY = 'programming_research_test/'

    def test_search_in_python_org(self):
        self.do_log(
            'Executing ProgrammingResearchTest.test_search_in_python_org')
        driver = self.webdriver

        # open a new browser and go to python.org
        driver.get('http://www.python.org')

        # taking screenshot
        self.do_screenshot()

        # check if title has 'Python' word in it
        self.assertIn('Python', driver.title)

        # do a research
        search_box = driver.find_element_by_name('q')
        search_box.clear()
        search_box.send_keys('pycon')
        self.do_break_time()
        search_box.send_keys(Keys.RETURN)

        # ensure that some results are found
        assert 'No results found.' not in driver.page_source

    def test_search_in_php_net(self):
        self.do_log('Executing ProgrammingResearchTest.test_search_in_php_net')
        driver = self.webdriver

        # open a new browser and go to python.org
        driver.get('https://www.php.net/')

        # taking screenshot
        self.do_screenshot()

        # check if title has 'PHP' word in it
        self.assertIn('PHP', driver.title)

        # do a bad research
        bad_research = 'azerty'
        search_box = driver.find_element_by_name('pattern')
        search_box.clear()
        search_box.send_keys(bad_research)
        self.do_break_time()
        search_box.send_keys(Keys.RETURN)

        # ensure that no result is found
        #assert bad_research + ' doesn\'t exist' in driver.page_source

        # do a good research
        good_research = 'print_r'
        search_box = driver.find_element_by_name('pattern')
        search_box.clear()
        search_box.send_keys(good_research)
        search_box.send_keys(Keys.RETURN)

        # ensure that some results are found
        assert good_research + ' doesn\'t exist' not in driver.page_source
        assert good_research in driver.page_source
