"""Environment module for behave"""
from behave.model_core import Status
from main.core.requests_manager import RequestsManager
from main.core.example import Example


def before_all(context):
    """Before_all
    """
    context.example = Example()
    context.rm = RequestsManager()
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


def before_tag(context, tag):  # pylint: disable=W0613
    """Just a simple before_tag hook
    """


def after_tag(context, tag):  # pylint: disable=W0613
    """Just a simple after_tag hook
    """
    if tag == "delete.boards":
        context.rm.delete_request(f"/boards/{context.id_dictionary[tag.split('.')[-1]]}")
