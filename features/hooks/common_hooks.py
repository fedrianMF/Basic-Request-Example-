"""Module for hooks"""
from behave import fixture
from main.core.utils.api_constants import HttpMethods as method


@fixture
def delete_resource(context, endpoint, tag):
    """Basic hook to delete board

    :param context: Global context from behave
    :type context: obj
    :param tag: tag to be retrieved
    """
    context.rm.do_request(method.DELETE.value, endpoint,
                          id=context.id_dictionary[tag.split('.')[-1]])
