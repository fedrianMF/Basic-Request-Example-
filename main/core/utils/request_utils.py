"""class to request utilitaries"""


class RequestUtils:
    """Class defined to request Utils"""
    @staticmethod
    def generate_data(body):
        data = {}
        if body is not None:
            for row in body:
                data[str(row['key'])] = RequestUtils.parse(row['value'])
        return data

    @staticmethod
    def validate_body(body, expected_data):
        # validate body here
        pass

    @staticmethod
    def parse(value):
        parsed_params = {"True": "true", "False": "false", "None": None}
        return parsed_params.get(value) if value.lower() in parsed_params else value
