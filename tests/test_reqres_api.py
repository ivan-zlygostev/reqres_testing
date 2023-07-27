from lib.api.response_checker_api import ChecklistApi

import pytest


class TestApiReqres:

    @pytest.mark.test
    @pytest.mark.backend
    def test_get_list_of_users_without_param(self, get_users, get_api_version):
        res = get_users
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'user_list')
        ChecklistApi(res.json()['page']) \
            .assert_response_value(1)
        ChecklistApi(res.json()) \
            .assert_comparison_len('>=', 5)

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('get_users_paging', [2, 100], indirect=True)
    def test_get_list_of_users_paging(self, get_users_paging, get_api_version):
        res, page = get_users_paging
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'user_list')
        ChecklistApi(res.json()['page']) \
            .assert_response_value(page)
        ChecklistApi(res.json()) \
            .assert_comparison_len('>=', 5)

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('get_user', [2, 10], indirect=True)
    def test_get_user(self, get_user, get_api_version):
        res, user_id = get_user
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'get_user')
        ChecklistApi(res.json()['data']['id']) \
            .assert_response_value(user_id)
        ChecklistApi(res.json()) \
            .assert_comparison_len('>=', 1)

    @pytest.mark.test
    @pytest.mark.backend
    @pytest.mark.exceptions
    @pytest.mark.parametrize('get_user', [23], indirect=True)
    def test_get_user_not_found(self, get_user, get_api_version):
        res, _ = get_user
        ChecklistApi(res) \
            .status_code_should_be_404() \
            .body_should_be_empty_json()

    @pytest.mark.test
    @pytest.mark.backend
    def test_get_list_of_resources_without_param(self, get_resources, get_api_version):
        res = get_resources
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'resources_list')
        ChecklistApi(res.json()['page']) \
            .assert_response_value(1)
        ChecklistApi(res.json()) \
            .assert_comparison_len('>=', 5)

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('get_resource', [2, 10], indirect=True)
    def test_get_resource(self, get_resource, get_api_version):
        res, user_id = get_resource
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'get_resource')
        ChecklistApi(res.json()['data']['id']) \
            .assert_response_value(user_id)
        ChecklistApi(res.json()) \
            .assert_comparison_len('>=', 1)

    @pytest.mark.test
    @pytest.mark.backend
    @pytest.mark.exceptions
    @pytest.mark.parametrize('get_resource', [23], indirect=True)
    def test_get_resource_not_found(self, get_resource):
        res, _ = get_resource
        ChecklistApi(res) \
            .status_code_should_be_404() \
            .body_should_be_empty_json()

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('create_user', [
        {
            'name': 'morpheus',
            'job': 'leader'
        }
    ], indirect=True)
    def test_create_user(self, create_user, get_api_version):
        res, req_json = create_user
        ChecklistApi(res) \
            .status_code_should_be_201() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'create_user')
        ChecklistApi(res.json()['name']) \
            .assert_response_value(req_json['name'])
        ChecklistApi(res.json()['job']) \
            .assert_response_value(req_json['job'])
        ChecklistApi(res.json()) \
            .assert_response_len(4)

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('update_user', [
        {
            'json': {
                'name': 'morpheus',
                'job': 'zion resident'
            },
            'id': 2,
            'method': 'put'
        },
        {
            'json': {
                'name': 'morpheus',
                'job': 'zion resident'
            },
            'id': 2,
            'method': 'patch'
        }
    ], indirect=True)
    def test_update_user(self, update_user, get_api_version):
        res, req_json = update_user
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'update_user')
        ChecklistApi(res.json()['name']) \
            .assert_response_value(req_json['name'])
        ChecklistApi(res.json()['job']) \
            .assert_response_value(req_json['job'])
        ChecklistApi(res.json()) \
            .assert_response_len(3)

    @pytest.mark.test
    @pytest.mark.backend
    @pytest.mark.parametrize('delete_user', [2], indirect=True)
    def test_delete_user(self, delete_user):
        res = delete_user
        ChecklistApi(res) \
            .status_code_should_be_204() \
            .body_should_be_empty()

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('register', [
        {
            'email': 'eve.holt@reqres.in',
            'password': 'pistol'
        }
    ], indirect=True)
    def test_register(self, register, get_api_version):
        res = register
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'register')
        ChecklistApi(res.json()) \
            .assert_response_len(2)

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.exceptions
    @pytest.mark.parametrize('register', [
        {
            'email': 'sydney@fife'
        }
    ], indirect=True)
    def test_register_without_password(self, register, get_api_version):
        res = register
        ChecklistApi(res) \
            .status_code_should_be_400() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'error')
        ChecklistApi(res.json()['error']) \
            .assert_response_value('Missing password')
        ChecklistApi(res.json()) \
            .assert_response_len(1)

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('login', [
        {
            'email': 'eve.holt@reqres.in',
            'password': 'cityslicka'
        }
    ], indirect=True)
    def test_login(self, login, get_api_version):
        res = login
        print(res.json())
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'login')
        ChecklistApi(res.json()) \
            .assert_response_len(1)

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.exceptions
    @pytest.mark.parametrize('login', [
        {
            'email': 'peter@klaven'
        }
    ], indirect=True)
    def test_login_without_password(self, login, get_api_version):
        res = login
        ChecklistApi(res) \
            .status_code_should_be_400() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'error')
        ChecklistApi(res.json()['error']) \
            .assert_response_value('Missing password')
        ChecklistApi(res.json()) \
            .assert_response_len(1)

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('get_users_delays', [3], indirect=True)
    def test_get_list_of_users_delays(self, get_users_delays, get_api_version):
        res = get_users_delays
        ChecklistApi(res) \
            .status_code_should_be_200() \
            .content_type_should_be_json() \
            .body_should_be_json() \
            .json_should_be_validate_schema(get_api_version, 'user_list')
        ChecklistApi(res.json()) \
            .assert_comparison_len('>=', 5)
