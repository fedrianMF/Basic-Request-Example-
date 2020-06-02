"""Module driver_factory"""
from main.core.selenium.firefox import Firefox
from main.core.selenium.chrome import Chrome


class DriverFactory:  # pylint: disable=R0903
    """DriverFactory Class"""

    __driver = {
        'firefox': Firefox,
        'chrome': Chrome
    }

    @staticmethod
    def get_instance(browser, **kwargs):
        """This method is uses for cerate a instance of browser.

        Args:
            browser (string):  defines th browser to be seleted.

        Returns:
            webdriver  -- return a webdriver.
        """
        instance = DriverFactory.__driver[browser.lower()].initialize(browser=browser, **kwargs)
        return instance
