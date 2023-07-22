import pytest

from pytest_schema import schema

from schema_expected.schema import ExpectedSchema


class TestApiReqres:

    @pytest.mark.test
    @pytest.mark.backend
    def test_get_list_of_users_status_code(self, get_users):
        res = get_users
        assert res.status_code == 200

    @pytest.mark.test
    @pytest.mark.backend
    def test_get_list_of_users_content_type(self, get_users):
        res = get_users
        assert res.headers['Content-type'] == 'application/json; charset=utf-8'

    @pytest.mark.test
    @pytest.mark.backend
    def test_get_list_of_users_json(self, get_users):
        res = get_users
        assert res.json()

    @pytest.mark.test
    @pytest.mark.backend
    def test_get_list_of_users_json_schema(self, get_users):
        res = get_users
        expected_schema = ExpectedSchema.users_list
        assert schema(expected_schema) == res.json()

    @pytest.mark.test
    @pytest.mark.backend
    def test_get_list_of_users_page_default(self, get_users):
        res = get_users
        assert res.json()['page'] == 1

    @pytest.mark.test
    @pytest.mark.background
    @pytest.mark.parametrize('get_users_paging', [2, 3], indirect=True)
    def test_get_list_of_users_paging_status_code(self, get_users_paging):
        res, _ = get_users_paging
        assert res.status_code == 200

    @pytest.mark.test
    @pytest.mark.backend
    @pytest.mark.parametrize('get_users_paging', [2, 3], indirect=True)
    def test_get_list_of_users_paging_content_type(self, get_users_paging):
        res, _ = get_users_paging
        assert res.headers['Content-type'] == 'application/json; charset=utf-8'

    @pytest.mark.test
    @pytest.mark.backend
    @pytest.mark.parametrize('get_users_paging', [2, 3], indirect=True)
    def test_get_list_of_users_paging_json(self, get_users_paging):
        res, _ = get_users_paging
        assert res.json()

    @pytest.mark.test
    @pytest.mark.backend
    @pytest.mark.parametrize('get_users_paging', [2, 3], indirect=True)
    def test_get_list_of_users_paging_json_schema(self, get_users_paging):
        res, _ = get_users_paging
        expected_schema = ExpectedSchema.users_list
        assert schema(expected_schema) == res.json()

    @pytest.mark.test
    @pytest.mark.backend
    @pytest.mark.parametrize('get_users_paging', [2, 100], indirect=True)
    def test_get_list_of_users_paging_page_value(self, get_users_paging):
        res, page = get_users_paging
        print(res.json())
        assert res.json()['page'] == page
