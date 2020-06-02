"""Module for common steps"""
from behave import given  # pylint: disable=E0611
from main.trello.ui.pages.login_page import LoginPage
from main.trello.ui.pages.boards.boards_page import BoardsPage


@given('the "admin" user signs in')
def step_sign_in(context):
    """Sample login

    :param context: Global context from behave
    :type context: obj
    :param user_type: type of user to be logged on app
    :type user_type: string
    """
    context.login_page = LoginPage(context.driver)
    context.login_page.login_as_user("jose.ig.cabrera.b@gmail.com", "insecurepassword")
    context.boards_page = BoardsPage(context.driver)
