from element_body_expected.body_expected import BodyExpected

from lib.front.response_checker_front import ChecklistFront

import pytest


class TestFrontendReqres:

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    def test_check_list_of_examples(self, go_to_site):
        expected_list_of_examples = [
            'LIST USERS',
            'SINGLE USER',
            'SINGLE USER NOT FOUND',
            'LIST <RESOURCE>',
            'SINGLE <RESOURCE>',
            'SINGLE <RESOURCE> NOT FOUND',
            'CREATE',
            'UPDATE',
            'UPDATE',
            'DELETE',
            'REGISTER - SUCCESSFUL',
            'REGISTER - UNSUCCESSFUL',
            'LOGIN - SUCCESSFUL',
            'LOGIN - UNSUCCESSFUL',
            'DELAYED RESPONSE'
        ]
        reqres_main_page, _ = go_to_site
        list_of_examples = reqres_main_page.find_list_examples()
        ChecklistFront(element=list_of_examples) \
            .assert_element_exist() \
            .assert_list_len(len(expected_list_of_examples))
        for i in range(len(list_of_examples)):
            ChecklistFront(element=list_of_examples[i]) \
                .assert_element_text(expected_list_of_examples[i])

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('get_users_paging', [2], indirect=True)
    def test_click_list_users(self, click_list_users, go_to_site, get_users_paging):
        reqres_main_page, _ = click_list_users
        element_request = reqres_main_page.find_request()
        api_response, _ = get_users_paging
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/users?page=2')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.list_users_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('get_user', [2], indirect=True)
    def test_click_single_user(self, click_single_user, go_to_site, get_user):
        reqres_main_page, _ = click_single_user
        element_request = reqres_main_page.find_request()
        api_response, _ = get_user
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/users/2')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.single_user_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('get_user', [23], indirect=True)
    def test_click_single_user_not_found(self, click_single_user_not_found, go_to_site, get_user):
        reqres_main_page, _ = click_single_user_not_found
        element_request = reqres_main_page.find_request()
        api_response, _ = get_user
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/users/23')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json({}) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('404') \
            .assert_element_text(api_response_status_code)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    def test_click_list_resource(self, click_list_resource, go_to_site, get_resources):
        reqres_main_page, _ = click_list_resource
        element_request = reqres_main_page.find_request()
        api_response = get_resources
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/unknown')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.list_resource_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('get_resource', [2], indirect=True)
    def test_click_single_resource(self, click_single_resource, go_to_site, get_resource):
        reqres_main_page, _ = click_single_resource
        element_request = reqres_main_page.find_request()
        api_response, _ = get_resource
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/unknown/2')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.single_resource_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('get_resource', [23], indirect=True)
    def test_click_single_resource_not_found(self, click_single_resource_not_found, go_to_site, get_resource):
        reqres_main_page, _ = click_single_resource_not_found
        element_request = reqres_main_page.find_request()
        api_response, _ = get_resource
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/unknown/23')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json({}) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('404') \
            .assert_element_text(api_response_status_code)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('create_user', [{
        'name': 'morpheus',
        'job': 'leader'
    }], indirect=True)
    def test_click_create(self, click_create, go_to_site, create_user):
        expected_request_body = {
            'name': 'morpheus',
            'job': 'leader'
        }
        reqres_main_page, _ = click_create
        element_request = reqres_main_page.find_request()
        api_response, _ = create_user
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/users')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.create_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('201') \
            .assert_element_text(api_response_status_code)
        element_request_body = reqres_main_page.find_request_body()
        ChecklistFront(element=element_request_body) \
            .assert_element_text_like_json() \
            .assert_element_json(expected_request_body)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('update_user', [{
        'json': {
            'name': 'morpheus',
            'job': 'zion resident'
        },
        'id': 2,
        'method': 'put'
    }], indirect=True)
    def test_click_update_put(self, click_update_put, go_to_site, update_user):
        expected_request_body = {
            'name': 'morpheus',
            'job': 'zion resident'
        }
        reqres_main_page, _ = click_update_put
        element_request = reqres_main_page.find_request()
        api_response, _ = update_user
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/users/2')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.update_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)
        element_request_body = reqres_main_page.find_request_body()
        ChecklistFront(element=element_request_body) \
            .assert_element_text_like_json() \
            .assert_element_json(expected_request_body)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('update_user', [{
        'json': {
            'name': 'morpheus',
            'job': 'zion resident'
        },
        'id': 2,
        'method': 'patch'
    }], indirect=True)
    def test_click_update_patch(self, click_update_patch, go_to_site, update_user):
        expected_request_body = {
            'name': 'morpheus',
            'job': 'zion resident'
        }
        reqres_main_page, _ = click_update_patch
        element_request = reqres_main_page.find_request()
        api_response, _ = update_user
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/users/2')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.update_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)
        element_request_body = reqres_main_page.find_request_body()
        ChecklistFront(element=element_request_body) \
            .assert_element_text_like_json() \
            .assert_element_json(expected_request_body)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('delete_user', [2], indirect=True)
    def test_click_delete(self, click_delete, go_to_site, delete_user):
        reqres_main_page, _ = click_delete
        element_request = reqres_main_page.find_request()
        api_response = delete_user
        api_response_status_code = str(api_response.status_code)
        api_response_body = api_response.content.decode('utf-8')
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/users/2')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_empty() \
            .assert_element_string(api_response_body)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('204') \
            .assert_element_text(api_response_status_code)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('register', [{
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    }], indirect=True)
    def test_click_register_successful(self, click_register_successful, go_to_site, register):
        expected_request_body = {
            'email': 'eve.holt@reqres.in',
            'password': 'pistol'
        }
        reqres_main_page, _ = click_register_successful
        element_request = reqres_main_page.find_request()
        api_response = register
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/register')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.register_successful_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)
        element_request_body = reqres_main_page.find_request_body()
        ChecklistFront(element=element_request_body) \
            .assert_element_text_like_json() \
            .assert_element_json(expected_request_body)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('register', [{
        'email': 'sydney@fife'
    }], indirect=True)
    def test_click_register_unsuccessful(self, click_register_unsuccessful, go_to_site, register):
        expected_request_body = {
            'email': 'sydney@fife'
        }
        reqres_main_page, _ = click_register_unsuccessful
        element_request = reqres_main_page.find_request()
        api_response = register
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/register')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.register_unsuccessful_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('400') \
            .assert_element_text(api_response_status_code)
        element_request_body = reqres_main_page.find_request_body()
        ChecklistFront(element=element_request_body) \
            .assert_element_text_like_json() \
            .assert_element_json(expected_request_body)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('login', [{
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    }], indirect=True)
    def test_click_login_successful(self, click_login_successful, go_to_site, login):
        expected_request_body = {
            'email': 'eve.holt@reqres.in',
            'password': 'cityslicka'
        }
        reqres_main_page, _ = click_login_successful
        element_request = reqres_main_page.find_request()
        api_response = login
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/login')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.login_successful_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)
        element_request_body = reqres_main_page.find_request_body()
        ChecklistFront(element=element_request_body) \
            .assert_element_text_like_json() \
            .assert_element_json(expected_request_body)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('login', [{
        'email': 'peter@klaven'
    }], indirect=True)
    def test_click_login_unsuccessful(self, click_login_unsuccessful, go_to_site, login):
        expected_request_body = {
            'email': 'peter@klaven'
        }
        reqres_main_page, _ = click_login_unsuccessful
        element_request = reqres_main_page.find_request()
        api_response = login
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/login')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.login_unsuccessful_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('400') \
            .assert_element_text(api_response_status_code)
        element_request_body = reqres_main_page.find_request_body()
        ChecklistFront(element=element_request_body) \
            .assert_element_text_like_json() \
            .assert_element_json(expected_request_body)

    @pytest.mark.test
    @pytest.mark.frontend
    @pytest.mark.parametrize('go_to_site', ['Chrome', 'Firefox'], indirect=True)
    @pytest.mark.parametrize('get_users_delays', [3], indirect=True)
    def test_click_list_users_delay(self, click_list_users_delay, go_to_site, get_users_delays):
        reqres_main_page, _ = click_list_users_delay
        element_request = reqres_main_page.find_request()
        api_response = get_users_delays
        api_response_json = api_response.json()
        api_response_status_code = str(api_response.status_code)
        ChecklistFront(element=element_request) \
            .assert_element_exist() \
            .assert_element_text('/api/users?delay=3')
        element_response_body = reqres_main_page.find_invisible_response_body()
        ChecklistFront(element=element_response_body) \
            .assert_element_text_like_json() \
            .assert_element_json(BodyExpected.list_users_delay_body) \
            .assert_element_json(api_response_json)
        element_response_code = reqres_main_page.find_response_code()
        ChecklistFront(element=element_response_code) \
            .assert_element_exist() \
            .assert_element_text('200') \
            .assert_element_text(api_response_status_code)
