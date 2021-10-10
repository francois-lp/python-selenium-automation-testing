from model.drivers.abstract_webdriver import AbstractWebdriver
from selenium import webdriver
#from selenium.webdriver.edge.options import Options as EdgeOptions

class EdgeWebdriver(AbstractWebdriver):

    BROWSER_NAME = 'Edge'
    BROWSER_DRIVER_PATH = 'F:\Drivers\msedgedriver.exe'

    def get_browser_name(self):
        return self.BROWSER_NAME

    def get_browser_driver_path(self):
        return self.BROWSER_DRIVER_PATH

    """
  def get_browser_options(self):
    options = EdgeOptions()
    #options.setBinary('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe');
    #options.use_chromium = True
    #options.add_argument("headless")
    #options.add_argument("disable-gpu")
    return options
  """

    def get_webdriver(self):
        browser_webdriver_function = getattr(webdriver, self.browser_name)
        return browser_webdriver_function(
            executable_path=self.browser_driver_path)
