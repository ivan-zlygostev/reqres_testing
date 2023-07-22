from pytest_schema import And, Regex


class ExpectedSchema:
    # /users
    users_list = {
        'page': And(int, lambda n: n > 0),
        'per_page': And(int, lambda n: n > 0),
        'total': And(int, lambda n: n > 0),
        'data': [
            {
                'id': int,
                'email': Regex(r'.*?@.*?\.[A-Za-z]{2,6}'),
                'first_name': str,
                'last_name': str,
                'avatar': str
            }
        ]
    }
