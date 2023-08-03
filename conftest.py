from api.reqres_api import ReqresAPI

from front.reqres_pages import ReqresBase

import pytest


from selenium import webdriver


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


@pytest.fixture(scope='function')
def go_to_site(pytestconfig, request):
    host = pytestconfig.getoption('host')
    driver_select = request.param
    if driver_select == 'Chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
    elif driver_select == 'Firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--incognito')
        driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    reqres_main_page = ReqresBase(driver, host)
    reqres_main_page.go_to_url()
    yield reqres_main_page, driver
    driver.quit()


@pytest.fixture(scope='function')
def click_list_users(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_list_users()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_single_user(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_single_user()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_single_user_not_found(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_single_user_not_found()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_list_resource(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_list_resource()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_single_resource(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_single_resource()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_single_resource_not_found(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_single_resource_not_found()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_create(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_create()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_update_put(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_update_put()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_update_patch(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_update_patch()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_delete(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_delete()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_register_successful(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_register_successful()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_register_unsuccessful(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_register_unsuccessful()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_login_successful(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_login_successful()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_login_unsuccessful(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_login_unsuccessful()
    return reqres_main_page, driver


@pytest.fixture(scope='function')
def click_list_users_delay(go_to_site):
    reqres_main_page, driver = go_to_site
    reqres_main_page.click_list_users_delay()
    return reqres_main_page, driver
