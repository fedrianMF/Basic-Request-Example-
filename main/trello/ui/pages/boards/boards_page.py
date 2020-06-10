"""Module for BoardsPage"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.core.utils.logger.logger_decorator import Log

class BoardsPage:
    """BoardsPage
    """
    plus_btn = (By.CSS_SELECTOR, '[data-test-id*="create-menu"]')
    boards_section = (By.CSS_SELECTOR, '[class="content-all-boards"]')

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 60).until(EC.visibility_of(self.driver.find_element(*self.plus_btn)))

    @Log(__name__)
    def click_board(self, board_name):
        """Method to fill user and password

        Args:
            board (string):  board name
        """
        board_name = (By.CSS_SELECTOR, f"[class*='board'][title='{board_name}']")
        self.driver.find_element(*board_name).click()

    @Log(__name__)
    def click_menu(self, menu_name):
        """Method to click menu

        Args:
            menu (string):  menu name
        """
        self.driver.find_element(*self.plus_btn).click()
        create_menu = (By.XPATH, f"//span[contains(text(),'{menu_name}')]")
        self.driver.find_element(*create_menu).click()
