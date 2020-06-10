"""Log decorator Class
The main goal is to avoid repeat code to log our
classes and methods"""
import functools
from main.core.utils.logger import logger_python


class Log():
    """ Logging decorator that allows you to log with the
    specific logger of logging.conf.
    """
    def __init__(self, module=__name__):
        self.logger = logger_python.LOGGER
        self.module = module

    def __call__(self, func):
        """ Returns a wrapper that wraps func.
        The wrapper will log the entry and exit points of the function
        to set the different levels of debugger

        Args:
            func {function} -- function to be wrapped and decorated
        """
        # set logger if it was not set earlier

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """wrap logic of debugger

            Args:
                *args {dictionary} -- arguments dictionary get from function
                **kwargs {dictionary} -- dictionary get from function

            Returns:
                function -- return the same function after to be wrapped
            """

            try:
                self.logger.info("%s|===Executing %s", self.module,
                                 func.__name__)
                self.logger.debug("%s|===with args %s", self.module, kwargs)
                f_result = func(*args, **kwargs)
                if f_result:
                    self.logger.debug("%s|===return %s", self.module, f_result)
                return f_result
            except Exception as ex:
                self.logger.error("%s|***Exception on %s related with %s",
                                  self.module, func.__name__, ex)
                self.logger.critical("%s|*** %s",
                                     self.module,
                                     ex,
                                     exc_info=True)
                raise ex
            return f_result

        return wrapper
