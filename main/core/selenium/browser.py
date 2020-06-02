"""Module i_browser"""
from abc import ABCMeta, abstractstaticmethod


class Browser(metaclass=ABCMeta):  # pylint: disable=R0903
    """Browser class"""

    @abstractstaticmethod
    def initialize(**kwargs):

        """This method is uses for define the behavior.

        Raises:
            NotImplementedError: when the classes that implements this abstract
            instance don't implement this method.
        """
        raise NotImplementedError
