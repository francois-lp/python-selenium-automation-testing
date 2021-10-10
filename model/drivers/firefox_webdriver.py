from model.drivers.abstract_webdriver import AbstractWebdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class FirefoxWebdriver(AbstractWebdriver):

    BROWSER_NAME = 'Firefox'
    BROWSER_DRIVER_PATH = 'F:\Drivers\mozilla-geckodriver.exe'

    def get_browser_name(self):
        return self.BROWSER_NAME

    def get_browser_driver_path(self):
        return self.BROWSER_DRIVER_PATH

    def get_browser_options(self):
        options = FirefoxOptions()
        # options.add_argument("--headless") # make browser invisible
        return options
