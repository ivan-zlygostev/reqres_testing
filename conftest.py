from api.reqres_api import ReqresAPI

import pytest


def pytest_addoption(parser):
    parser.addoption('--host', action='store')
    parser.addoption('--api_version', action='store')


@pytest.fixture(scope='class')
def get_api_version(pytestconfig):
    return pytestconfig.getoption('api_version')


@pytest.fixture(scope='class')
def reqres_client(pytestconfig):
    client = ReqresAPI(host=pytestconfig.getoption('host'))
    return client


@pytest.fixture(scope='class')
def get_users(reqres_client):
    res = reqres_client.list_users()
    return res


@pytest.fixture(scope='class')
def get_users_paging(reqres_client, request):
    params = {
        'page': request.param
    }
    res = reqres_client.list_users(params=params)
    return res, request.param


@pytest.fixture(scope='class')
def get_users_delays(reqres_client, request):
    params = {
        'delay': request.param
    }
    res = reqres_client.list_users(params=params)
    return res


@pytest.fixture(scope='class')
def get_user(reqres_client, request):
    user_id = request.param
    res = reqres_client.fetches_user(user_id=user_id)
    return res, user_id


@pytest.fixture(scope='class')
def get_resources(reqres_client):
    res = reqres_client.list_resources()
    return res


@pytest.fixture(scope='class')
def get_resource(reqres_client, request):
    resource_id = request.param
    res = reqres_client.fetches_resource(resource_id=resource_id)
    return res, resource_id


@pytest.fixture(scope='class')
def create_user(reqres_client, request):
    req_json = request.param
    res = reqres_client.create_user(json=req_json)
    return res, req_json


@pytest.fixture(scope='class')
def update_user(reqres_client, request):
    req_json = request.param['json']
    user_id = request.param['id']
    method = request.param['method']
    if method == 'put':
        res = reqres_client.update_user_method_put(user_id=user_id, json=req_json)
    elif method == 'patch':
        res = reqres_client.update_user_method_patch(user_id=user_id, json=req_json)
    return res, req_json


@pytest.fixture(scope='class')
def delete_user(reqres_client, request):
    user_id = request.param
    res = reqres_client.delete_user(user_id=user_id)
    return res


@pytest.fixture(scope='class')
def register(reqres_client, request):
    req_json = request.param
    res = reqres_client.register(json=req_json)
    return res


@pytest.fixture(scope='class')
def login(reqres_client, request):
    req_json = request.param
    res = reqres_client.login(json=req_json)
    return res
