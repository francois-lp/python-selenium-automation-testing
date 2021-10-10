from model.tests.abstract_test import AbstractTest

class SiteRunnersTest(AbstractTest):

    CONFIG_OUTPUT_TEST_DIRECTORY = 'urban_challenge_test/'

    def test_menu(self):
        self.do_log('Executing SiteRunnersTest.test_menu')
        driver = self.webdriver

        # open a new browser and go to python.org
        driver.get('https://blog.urban-challenge.fr')

        # taking screenshot
        self.do_screenshot()

        # check menu
        menu = driver.find_element_by_id('cb-nav-bar')
        self.assertIsNotNone(menu)
