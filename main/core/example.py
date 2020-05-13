"""Simple class Example"""


class Example:
    """Just an example class to be deleted
    """

    def __init__(self):
        """Initialize
        """
        self.first_number = 1
        self.second_number = 2
        self.result = 3

    def get_first_number(self):
        """Getter
        """
        return self.first_number

    def set_first_number(self, value):
        """Setter
        """
        self.first_number = int(value)

    def get_second(self):
        """Getter
        """
        return self.second_number

    def set_second_number(self, value):
        """Setter
        """
        self.second_number = int(value)

    def get_result(self):
        """Getter
        """
        return self.result

    def set_result(self, value):
        """Setter
        """
        self.result = int(value)

    def add_two_values(self):
        """Function to add two values

        :return: Addition of two values
        :rtype: int
        """
        result = self.first_number + self.second_number
        return result
