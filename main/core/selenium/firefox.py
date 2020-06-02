"""Module firefox"""
from selenium import webdriver
from main.core.selenium.browser import Browser


class Firefox(Browser):  # pylint: disable=R0903
    """Firefox class"""
    type_browser = None

    @staticmethod
    def initialize(**kwargs):
        """This method initialices a instance of Firefox.

        Returns:
            driver: return the webdriver for firefox
        """
        Firefox.type_browser = webdriver.Firefox()
        return Firefox.type_browser
