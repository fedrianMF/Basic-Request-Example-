"""Module for LoginPage"""
from selenium.webdriver.common.by import By


class LoginPage:
    """LoginPage
    """
    username_txt = (By.ID, 'user')
    password_txt = (By.ID, 'password')
    log_in_btn = (By.ID, 'login')

    def __init__(self, driver):
        self.driver = driver

    def login_as_user(self, user, password):
        """Method to fill user and password

        Args:
            user (string):  user name
            password (string):  user password
        """
        self.driver.find_element(*self.username_txt).clear()
        self.driver.find_element(*self.username_txt).send_keys(user)
        self.driver.find_element(*self.password_txt).clear()
        self.driver.find_element(*self.password_txt).send_keys(password)
        self.click_login()

    def click_login(self):
        """Click login button

        """
        self.driver.find_element(*self.log_in_btn).click()
