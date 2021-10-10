from model.drivers.abstract_webdriver import AbstractWebdriver
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options as ChromeOptions

class ChromeWebdriver(AbstractWebdriver):

    BROWSER_NAME = 'Chrome'
    BROWSER_DRIVER_PATH = 'F:\Drivers\chromedriver.exe'

    def get_browser_name(self):
        return self.BROWSER_NAME

    def get_browser_driver_path(self):
        return self.BROWSER_DRIVER_PATH

    def get_browser_options(self):
        """
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile': {
                'password_manager_enabled': False
            }
        })
        """
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.set_capability('--headless', False)
        #chrome_options.set_capability('--start-maximized', True)
        #chrome_options.headless = True
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--remote-debugging-port=9222")
        # chrome_options.add_argument('--no-sandbox')
        return chrome_options

    def get_webdriver(self):
        browser_webdriver_function = getattr(webdriver, self.browser_name)
        return browser_webdriver_function(
            executable_path=self.browser_driver_path,
            chrome_options=self.browser_options)
