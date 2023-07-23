from lib.api.content_type import content_type
from lib.api.status_code import status_code

from pytest_schema import schema

from requests import Response

from schema_expected.schema import api_versions_schema


class ChecklistApi:

    def __init__(self, response: Response):
        self.response = response

    def status_code(self, status_code: int):
        res_status_code = self.response.status_code
        assert res_status_code == status_code, f'Status code is {res_status_code}, expected {status_code}'
        return self

    def status_code_should_be_200(self):
        self.status_code(status_code.SUCCESS)
        return self

    def status_code_should_be_201(self):
        self.status_code(status_code.CREATED)
        return self

    def status_code_should_be_400(self):
        self.status_code(status_code.BAD_REQUEST)
        return self

    def status_code_should_be_401(self):
        self.status_code(status_code.BAD_CREDENTIALS)
        return self

    def status_code_should_be_409(self):
        self.status_code(status_code.CONFLICT)
        return self

    def status_code_should_be_403(self):
        self.status_code(status_code.FORBIDDEN)
        return self

    def status_code_should_be_404(self):
        self.status_code(status_code.NOT_FOUND)
        return self

    def status_code_should_be_405(self):
        self.status_code(status_code.METHOD_NOT_ALLOWED)
        return self

    def status_code_should_be_406(self):
        self.status_code(status_code.NOT_ACCEPTABLE)
        return self

    def status_code_should_be_415(self):
        self.status_code(status_code.UNSUPPORTED_MEDIA_TYPE)
        return self

    def status_code_should_be_500(self):
        self.status_code(status_code.INTERNAL_SERVER_ERROR)
        return self

    def content_type(self, val: str):
        if 'Content-Type' in self.response.headers:
            res_content_type = self.response.headers['Content-Type'].lower().replace(' ', '')
        else:
            res_content_type = None
        assert res_content_type in val.lower(), f'Response Content type is {res_content_type}, expected {val.lower()}'
        return self

    def content_type_should_be_json(self):
        self.content_type(content_type.JSON)
        return self

    def body_should_be_json(self):
        assert self.response.json(), 'Response body is not Json'
        return self

    def json_should_be_validate_schema(self, api_version: str, json_schema: str):
        expected_schema = api_versions_schema[api_version][json_schema]
        assert schema(expected_schema) == self.response.json()
        return self

    def assert_response_value(self, expected_value):
        assert self.response == expected_value, f'expected value != actual result ({expected_value} != {self.response})'
        return self

    def assert_comparison_len(self, comparison_operator: str, length: int):
        if comparison_operator == '>' or comparison_operator == 'more' or comparison_operator == 'greater than':
            assert len(self.response) > length, f'expected len {length} not more {len(self.response)}'
        elif comparison_operator == '<' or comparison_operator == 'less' or comparison_operator == 'less than':
            assert len(self.response) < length, f'expected len {length} not less {len(self.response)}'
        elif comparison_operator == '>=' or comparison_operator == 'more or equal':
            assert len(self.response) >= length, f'expected len {length} not more or equal {len(self.response)}'
        elif comparison_operator == '<=' or comparison_operator == 'less or equal':
            assert len(self.response) <= length, f'expected len {length} not less or equal {len(self.response)}'
        else:
            raise Exception('incorrect comparison_operator')
        return self
