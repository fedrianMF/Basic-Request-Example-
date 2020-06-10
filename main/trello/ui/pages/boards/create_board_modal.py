"""Module for CreateBoardModal"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.core.utils.logger.logger_decorator import Log

class CreateBoardModal:
    """CreateBoardModal
    """
    create_board_btn = (By.CSS_SELECTOR, '[data-test-id*="create-board-submit"]')
    board_title_txt = (By.CSS_SELECTOR, '[data-test-id*="board-title"]')

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 60).until(
                                             EC.visibility_of(self.driver.find_element(*self.board_title_txt)))

    @Log(__name__)
    def create_board(self, board):
        """Method to fill board_name and create board

        Args:
            board (string):  board name
        """
        self.driver.find_element(*self.board_title_txt).send_keys(board.name)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.create_board_btn))
        self.driver.find_element(*self.create_board_btn).click()
        WebDriverWait(self.driver, 60).until(EC.staleness_of(self.driver.find_element(*self.create_board_btn)))
