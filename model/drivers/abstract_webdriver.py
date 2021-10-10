from abc import ABC, abstractmethod
from selenium import webdriver
from typing import final

class AbstractWebdriver(ABC):

    @final
    def __init__(self):
        self.browser_name = self.get_browser_name()
        self.browser_driver_path = self.get_browser_driver_path()
        self.browser_options = self.get_browser_options()

    @abstractmethod
    def get_browser_name(self):
        pass

    @abstractmethod
    def get_browser_driver_path(self):
        pass

    # can be overridden by child class
    def get_webdriver(self):
        browser_webdriver_function = getattr(webdriver, self.browser_name)
        return browser_webdriver_function(
            executable_path=self.browser_driver_path,
            options=self.browser_options)

    # can be overridden by child class
    def get_browser_options(self):
        return ''
