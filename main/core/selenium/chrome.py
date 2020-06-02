"""Module chrome"""
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from main.core.selenium.browser import Browser


class Chrome(Browser):  # pylint: disable=R0903
    """Chrome class"""
    type_browser = None

    @staticmethod
    def initialize(**kwargs):
        """This method initialices a instance of Chrome.

        Returns:
            driver: return the webdriver for Chrome
        """
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities['acceptInsecureCerts'] = True
        Chrome.type_browser = webdriver.Chrome(desired_capabilities=desired_capabilities)
        return Chrome.type_browser
