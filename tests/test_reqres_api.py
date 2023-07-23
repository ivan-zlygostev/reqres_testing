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
