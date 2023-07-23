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
