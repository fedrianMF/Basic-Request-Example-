"""Module for example steps"""
from behave import when, then, step  # pylint: disable=E0611
from assertpy import assert_that
from dataclasses import asdict

from main.trello.ui.pages.boards.create_board_modal import CreateBoardModal
from main.trello.ui.pages.boards.board_details_page import BoardDetailsPage
from main.core.utils.request_utils import RequestUtils as req
from main.trello.ui.entities.board import Board

@when('the user clicks on "{button_name}" button')
def step_retrieve_numbers_dt(context, button_name):
    """Sample step to retrieve numbers

    :param context: Global context from behave
    :type context: obj
    """
    context.boards_page.click_menu(button_name)
    context.create_board_modal = CreateBoardModal(context.driver)


@step('the user creates Board with')
def step_create_board(context):
    """Sample step to fill board info

    :param context: Global context from behave
    :type context: obj
    """
    board_title = req.generate_data(context.table)['BoardTitle']
    context.boardEntity = Board(name=board_title)
    context.create_board_modal.create_board(context.boardEntity)
    context.board_details_page = BoardDetailsPage(context.driver)
    # context.id_dictionary["/boards"] = getBoardID(board_title)


@then('the following board info must appears in Board Details')
def step_verify_board_details(context):
    """
        Verify Details of an specic Board
    """
    expected_board = asdict(context.boardEntity)
    expected_message = f"Expected that {context.board_details_page.get_board_info()}\
                        is in {expected_board.items()}"
    assert_that(context.board_details_page.get_board_info().items() <= expected_board.items(),
                expected_message).is_true()
