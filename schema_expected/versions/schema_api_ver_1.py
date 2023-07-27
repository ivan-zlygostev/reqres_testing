from pytest_schema import And, Optional, Regex


class ExpectedSchema:

    optional = {
        Optional('support'): {
            'url': str,
            'text': str
        }
    }
    pages = {
        'page': And(int, lambda n: n > 0),
        'per_page': And(int, lambda n: n > 0),
        'total': And(int, lambda n: n > 0)
    }
    user = {
        'id': int,
        'email': Regex(r'.*?@.*?\.[A-Za-z]{2,6}'),
        'first_name': str,
        'last_name': str,
        'avatar': str
    }
    resource = {
        'id': int,
        'name': str,
        'year': And(int, lambda n: n > 0),
        'color': str,
        'pantone_value': str
    }
    create_user = {
        'name': str,
        'job': str,
        'id': str,
        'createdAt': str
    }
    update_user = {
        'name': str,
        'job': str,
        'updatedAt': str
    }
    register = {
        'id': And(int, lambda n: n > 0),
        'token': str
    }
    login = {
        'token': str
    }
    error = {
        'error': str
    }
    user_list = {
        'data': [
            user
        ]
    }
    user_list.update(pages)
    user_list.update(optional)

    get_user = {
        'data': user,
    }
    get_user.update(optional)

    resources_list = {
        'data': [resource]
    }
    resources_list.update(pages)
    resources_list.update(optional)

    get_resource = {
        'data': resource
    }
    get_resource.update(optional)


expected_schemas = {
    'user_list': ExpectedSchema.user_list,
    'get_user': ExpectedSchema.get_user,
    'resources_list': ExpectedSchema.resources_list,
    'get_resource': ExpectedSchema.get_resource,
    'create_user': ExpectedSchema.create_user,
    'update_user': ExpectedSchema.update_user,
    'register': ExpectedSchema.register,
    'login': ExpectedSchema.login,
    'error': ExpectedSchema.error
}
