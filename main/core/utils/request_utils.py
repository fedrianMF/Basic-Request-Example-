"""class to request utilities"""


class RequestUtils:
    """Class defined to request Utils"""
    @staticmethod
    def generate_data(body):
        """
            Method to generate body
        """
        data = {}
        if body is not None:
            for row in body:
                data[str(row['key'])] = RequestUtils.parse(row['value'])
        return data

    @staticmethod
    def validate_body(body, expected_data):
        """
            Method to validate body
        """

    @staticmethod
    def parse(value):
        """
            Method to parse body
        """
        parsed_params = {"True": "true", "False": "false", "None": None}
        return parsed_params.get(value) if value.lower() in parsed_params else value
