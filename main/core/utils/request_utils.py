
class RequestUtils:
    """Class defined to request Utils"""
    @staticmethod
    def generate_data(body):
        data = {}
        if body is not None:
            for row in body:
                data[str(row['key'])] = row['value']
        return data

    @staticmethod
    def validate_body(body, expected_data):
        # validate body here
        pass
