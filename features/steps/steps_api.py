"""Module for example steps"""
from behave import step, use_step_matcher  # pylint: disable=E0611
from assertpy import assert_that
from main.core.utils.request_utils import RequestUtils as utils
from main.core.utils.api_constants import HttpMethods as method


use_step_matcher("re")


@step(u'Defines "(?P<http_method>GET|POST|PUT|DELETE)" request to "(?P<endpoint>.*)"')
def step_retrieve_numbers_dt(context, http_method, endpoint):
    """Sample step to retrieve numbers

    :param context: Global context from behave
    :type context: obj
    :param http_method: HTTP method
    :type http_method: string
    :param endpoint: Application's endpoint method
    :type endpoint: obj
    """
    context.endpoint = endpoint
    context.data_table = context.table
    context.http_method = http_method


use_step_matcher("parse")


@step(u"The request is sent")
def step_impl_send(context):
    """Sends request

    :param context: Global context from behave
    :type context: obj
    """
    context.status_code, context.json_response = context.rm.do_request(context.http_method,
                                                                       context.endpoint,
                                                                       context.data_table)
    if context.http_method == method.POST.value:
        context.id_dictionary[context.endpoint.replace("/", "")] = context.json_response["id"]


@step(u'The status code should be {status_code:d}')
def step_impl_status(context, status_code):
    """Sends request

    :param context: Global context from behave
    :type context: obj
    :param status_code: status code retrieved
    :type status_code: int
    """
    assert_that(context.status_code).is_equal_to(status_code)


@step(u'Validates response body with')
def step_impl_validate_body(context):
    """Sends request

    :param context: Global context from behave
    :type context: obj
    """
    body = utils.generate_data(context.table)
    assert_that(body.items() <= context.json_response.items(),
                f"Expected that {body} is in {context.json_response}").is_true()
    # BodyValidator.validate(context.json_response, context.table)
