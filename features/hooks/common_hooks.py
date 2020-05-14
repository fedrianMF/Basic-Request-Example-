"""Module for hooks"""


def use_fixture_by_tag(tag, context, fixture_registry):  # pylint: disable=W0613
    """Method to use fixture and filter by a tag value

    Args:
        context (Context): Context
        fixture_registry (str): Fixture to be search
    """
    fixture_data = fixture_registry.get(tag, None)
    if fixture_data is None:
        raise LookupError("Unknown fixture-tag: %s" % tag)
    return fixture_data(context)
