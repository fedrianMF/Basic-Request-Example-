"""Environment module for behave"""
from behave.model_core import Status
from behave.fixture import use_fixture_by_tag, fixture_call_params
from main.core.selenium.driver_factory import DriverFactory
from main.core.requests.requests_manager import RequestsManager
from main.core.example import Example
from features.hooks.common_hooks import delete_resource


def before_all(context):
    """Before_all
    """
    context.example = Example()
    context.rm = RequestsManager.get_instance()
    context.driver = DriverFactory.get_instance("Chrome")
    context.driver.set_page_load_timeout(60)
    context.driver.implicitly_wait(15)
    context.driver.maximize_window()
    context.driver.get("https://trello.com/login")
    context.id_dictionary = {}


def before_scenario(context, scenario):  # pylint: disable=W0613
    """Before scenario hook
    """
    print(f"=============Started {scenario.name}")


def after_scenario(context, scenario):  # pylint: disable=W0613
    """After scenario hook if the scenario is failed take a screenshot
    """
    if scenario.status == Status.failed:
        print(f"============ Ooops Failed scenario {scenario.name}")
    print(f"=============Finished {scenario.name}")


def before_feature(context, feature):  # pylint: disable=W0613
    """Before feature hook
    """


def after_feature(context, feature):  # pylint: disable=W0613
    """after feature hook
    """


FIXTURE_REGISTRY = {
    "fixture.delete.boards": fixture_call_params(delete_resource,
                                                 endpoint="/boards",
                                                 tag="fixture.delete.boards")
}


def before_tag(context, tag):  # pylint: disable=W0613
    """Just a simple before_tag hook
    """


def after_tag(context, tag):  # pylint: disable=W0613, R1710
    """Just a simple after_tag hook
    """
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, FIXTURE_REGISTRY)


def after_all(context):
    """Before_all
    """
    context.driver.quit()
    context.rm.close_session()
