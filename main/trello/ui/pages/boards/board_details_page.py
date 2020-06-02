"""Module for BoardDetails"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BoardDetailsPage:
    """BoardDetails
    """
    permission_level_lbl = (By.CSS_SELECTOR, '#permission-level [class*="text"]')
    board_title_lbl = (By.CSS_SELECTOR, '[class*="rename-board"] [class*="text"]')

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.board_title_lbl))

    def get_board_info(self):
        """Method to get board info
        """
        return {"BoardTitle": self.driver.find_element(*self.board_title_lbl).text,
                "Privacy": self.driver.find_element(*self.permission_level_lbl).text}
