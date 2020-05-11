"""Module for example steps"""
from behave import given, when, then  # pylint: disable=E0611
from assertpy import assert_that


@given('The numbers are set')
def step_retrieve_numbers_dt(context):
    """Sample step to retrieve numbers

    :param context: Global context from behave
    :type context: obj
    """
    for row in context.table:
        context.example.set_first_number(row["number1"])
        context.example.set_second_number(row["number2"])


@given('The numbers "{firstNumber}" and "{secondNumber}" are set')
def step_retrieve_numbers(context, first_number, second_number):
    """Sample step to retrieve numbers

    :param context: Global context from behave
    :type context: obj
    :param first_number: The first number
    :type first_number: int
    :param second_number: The second number
    :type second_number: int
    """
    context.example.set_first_number(first_number)
    context.example.set_second_number(second_number)


@when('These numbers are added up')
def step_test2(context):
    """Step that adds two numbers

    :param context: Global context from behave
    :type context: obj
    """
    actual = context.example.add_two_values()
    context.example.set_result(actual)


@then('the result is "{expected}"')
def stesp_test3(context, expected):
    """Step to return addition of numbers

    :param context: Global context from behave
    :type context: obj
    :param expected: exptected value to be returned
    :type expected: int
    """
    actual = context.example.get_result()
    expected = int(expected)
    assert_that(actual).is_equal_to(expected)
