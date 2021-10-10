import globals_vars
import logging
import time
import unittest
from datetime import datetime
from typing import final
from model.drivers.chrome_webdriver import ChromeWebdriver
from model.drivers.edge_webdriver import EdgeWebdriver
from model.drivers.firefox_webdriver import FirefoxWebdriver

class AbstractTest(unittest.TestCase):

    CONFIG_BREAK_TIME = 5
    CONFIG_OUTPUT_TEST_DIRECTORY = ''

    OUTPUT_ROOT_DIRECTORY = 'output/'
    OUTPUT_LOGS_DIRECTORY = OUTPUT_ROOT_DIRECTORY + 'logs/'
    OUTPUT_SCREENSHOTS_DIRECTORY = OUTPUT_ROOT_DIRECTORY + 'screenshots/'

    DATETIME_FILE_FORMAT = '%Y%m%d_%H%M%S'
    DATETIME_LOGS_FORMAT = '%Y-%m-%d %H:%M:%S'

    @final
    def __init__(self, *args, **kwargs):
        self.set_config()
        self.set_webdriver()
        self.set_logger()
        unittest.TestCase.__init__(self, *args, **kwargs)

    @final
    def set_webdriver(self):
        browser_name = globals_vars.browser_name
        if(browser_name == 'Chrome'):
            self.webdriver = ChromeWebdriver().get_webdriver()
        elif(browser_name == 'Firefox'):
            self.webdriver = FirefoxWebdriver().get_webdriver()
        elif(browser_name == 'Edge'):
            self.webdriver = EdgeWebdriver().get_webdriver()
        else:
            print('Webdriver error')

    @final
    def set_config(self):
        self.config_break_time = self.CONFIG_BREAK_TIME
        self.config_screenshots_directory = self.OUTPUT_SCREENSHOTS_DIRECTORY + \
            self.CONFIG_OUTPUT_TEST_DIRECTORY

    @final
    def set_logger(self):
        logging.basicConfig(
            filename=self.OUTPUT_LOGS_DIRECTORY +
            self.get_current_datetime(
                self.DATETIME_FILE_FORMAT) + '_test_logs.log',
            format='%(asctime)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filemode='w'
        )
        logging.getLogger().setLevel(logging.INFO)
        self.logging = logging
        #logging.info('This is an info message')

    @final
    def get_current_datetime(self, format=DATETIME_LOGS_FORMAT):
        return (datetime.now()).strftime(format)

    @classmethod
    def setUpClass(cls):
        cls.do_log(cls, 'Start class tests')

    @final
    def setUp(self):
        self.do_log('Start function test')

    @final
    def tearDown(self):
        self.do_log('End function test')
        self.webdriver.close()

    @classmethod
    def tearDownClass(cls):
        cls.do_log(cls, 'End class tests')

    @final
    def do_log(self, message):
        print(self.get_current_datetime(
            self.DATETIME_LOGS_FORMAT) + ' - ' + message)
        logging.info(message)

    @final
    def do_screenshot(self):
        self.webdriver.get_screenshot_as_file(
            self.config_screenshots_directory + 'screenshot_' + self.get_current_datetime(self.DATETIME_FILE_FORMAT) + '.png')

    # can be overridden by child class
    def do_break_time(self):
        time.sleep(self.config_break_time)
