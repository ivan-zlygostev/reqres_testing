import copy
import json

from selenium import webdriver


class ChecklistFront:

    def __init__(self, driver: webdriver = None, element=None):
        self.driver = driver
        self.element = element

    def assert_current_url(self, expected_url):
        assert self.driver.current_url == expected_url, f'expected value != \
            actual result ({expected_url} != {self.driver.current_url})'
        return self

    def assert_element_exist(self):
        assert self.element is not None, 'not found element'
        return self

    def assert_list_len(self, expected_len):
        assert len(self.element) == expected_len, f'expected len != actual len ({expected_len} != {len(self.element)})'
        return self

    def assert_element_text(self, expected_value):
        assert self.element.text == expected_value, f'expected value != actual result ({expected_value} != {self.element.text})'
        return self

    def assert_element_text_like_json(self):
        if self.element.text == '{}':
            assert True
        else:
            assert json.loads(self.element.text), f'element text not json {self.element.text}'
        return self

    def check_create_date_create_in_json(self, actual_result, expected_json):
        actual_result_copy = copy.deepcopy(actual_result)
        expected_json_copy = copy.deepcopy(expected_json)
        if 'createdAt' in actual_result and 'createdAt' in expected_json:
            actual_result_copy.pop('createdAt')
            expected_json_copy.pop('createdAt')
        return actual_result_copy, expected_json_copy

    def check_id_in_json(self, actual_result, expected_json):
        actual_result_copy = copy.deepcopy(actual_result)
        expected_json_copy = copy.deepcopy(expected_json)
        if 'id' in actual_result and 'id' in expected_json:
            actual_result_copy.pop('id')
            expected_json_copy.pop('id')
        return actual_result_copy, expected_json_copy

    def check_update_date_create_in_json(self, actual_result, expected_json):
        actual_result_copy = copy.deepcopy(actual_result)
        expected_json_copy = copy.deepcopy(expected_json)
        if 'updatedAt' in actual_result and 'updatedAt' in expected_json:
            actual_result_copy.pop('updatedAt')
            expected_json_copy.pop('updatedAt')
        return actual_result_copy, expected_json_copy

    def assert_element_json(self, expected_json):
        if self.element.text == '{}':
            actual_result = {}
        else:
            actual_result = json.loads(self.element.text)
        actual_result, expected_json = self.check_create_date_create_in_json(actual_result=actual_result,
                                                                             expected_json=expected_json)  # remove field "createdAt"
        actual_result, expected_json = self.check_id_in_json(actual_result=actual_result,
                                                             expected_json=expected_json)  # remove field "id"
        actual_result, expected_json = self.check_update_date_create_in_json(actual_result=actual_result,
                                                                             expected_json=expected_json)  # remove field "updatedAt"
        assert actual_result == expected_json, f'expected value != actual result \
            ({expected_json} != {actual_result})'
        return self

    def assert_element_empty(self):
        assert self.element.text == '', f'element no empty - {self.element.text}'
        return self

    def assert_element_string(self, expected_string):
        assert self.element.text == expected_string, f'expected value != actual result ({expected_string} != {self.element.text})'
        return self
