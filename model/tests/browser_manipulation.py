from model.tests.abstract_test import AbstractTest
from datetime import datetime
import time

class BrowserManipulation(AbstractTest):

    CONFIG_BREAK_TIME = 1
    CONFIG_OUTPUT_DIRECTORY = 'browser_manipulation/'

    # overriding AbstractTest function (sleep 1 second instead of 5)
    def do_break_time(self):
        time.sleep(self.CONFIG_BREAK_TIME)

    # overriding AbstractTest function
    def get_output_directory(self):
        return self.CONFIG_OUTPUT_DIRECTORY

    def execute_tests(self):
        # open browser
        driver = self.webdriver
        driver.set_page_load_timeout(10)
        driver.maximize_window()
        driver.get('https://duckduckgo.com/')
        self.do_break_time()

        # write in input search (voluntary typo)
        search_box = driver.find_element_by_xpath(
            '//*[@id="search_form_input_homepage"]')
        search_box.clear()
        search_box.send_keys('Python tutoraill')
        self.do_break_time()

        # click on search button
        search_button = driver.find_element_by_xpath(
            '//*[@id="search_button_homepage"]')
        search_button.click()
        self.do_break_time()
        # or just ENTER
        # search_box.send_keys(Keys.RETURN)

        # click on spelling suggestion
        search_button = driver.find_element_by_xpath(
            '//*[@class="js-spelling-suggestion-link"]')
        search_button.click()
        self.do_break_time()

        # scroll down
        # scroll vertically down by 300 pixels the first time
        driver.execute_script('window.scrollBy(0,300)')
        self.do_break_time()
        # scroll vertically down by 300 pixels the second time
        driver.execute_script('window.scrollBy(0,600)')
        self.do_break_time()
        driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)')  # scroll to bottom
        self.do_break_time()

        # taking screenshot
        current_datetime = (datetime.now()).strftime('%Y%m%d_%H%M%S')
        driver.get_screenshot_as_file(
            self.config_output_directory + 'screenshot_' + current_datetime + '.png')

        # open second tab
        driver.execute_script('window.open()')
        driver.switch_to.window(driver.window_handles[1])
        self.do_break_time()

        # change page
        driver.get('https://www.php.net/')
        self.do_break_time()

        # refresh page
        driver.refresh()
        self.do_break_time()

        # return to first tab
        driver.switch_to.window(driver.window_handles[0])

        # change page
        driver.get('https://python.org')
        self.do_break_time()
        driver.get('https://pypi.org/')
        self.do_break_time()

        # navigate
        driver.back()
        self.do_break_time()
        driver.forward()
        self.do_break_time()

        # close browser
        driver.quit()

        # status message
        print('Script executed successfully !')
