from front.reqres_front import ReqresFrontBase

from selenium.webdriver.common.by import By


class ReqresLocator:
    CSS_TRY_API_LINKS = 'body div.container div.home-content div.wrap section#console.console.try-api-links'
    CSS_EXAMPLES_LIST = CSS_TRY_API_LINKS + " div.endpoints[data-key='endpoints'] ul li"
    LOCATOR_EXAMPLES_LIST = (By.CSS_SELECTOR, CSS_EXAMPLES_LIST)
    LOCATOR_LIST_USERS = (By.CSS_SELECTOR, "[href='/api/users?page=2']")
    LOCATOR_SINGLE_USER = (By.CSS_SELECTOR, "[href='/api/users/2']")
    LOCATOR_SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, "[href='/api/users/23']")
    LOCATOR_LIST_RESOURCE = (By.CSS_SELECTOR, "[href='/api/unknown']")
    LOCATOR_SINGLE_RESOURCE = (By.CSS_SELECTOR, "[href='/api/unknown/2']")
    LOCATOR_SINGLE_RESOURCE_NOT_FOUND = (By.CSS_SELECTOR, "[href='/api/unknown/23']")
    LOCATOR_CREATE = (By.CSS_SELECTOR, "[data-id='post'][data-key='endpoint'] \
                      a[data-key='try-link'][href='/api/users']")
    LOCATOR_UPDATE_PUT = (By.CSS_SELECTOR, "[data-http='put'][data-id='put'][data-key='endpoint'] \
                          a[data-key='try-link'][href='/api/users/2']")
    LOCATOR_UPDATE_PATCH = (By.CSS_SELECTOR, "[data-http='patch'][data-id='patch'][data-key='endpoint'] \
                            a[data-key='try-link'][href='/api/users/2']")
    LOCATOR_DELETE = (By.CSS_SELECTOR, "[data-http='delete'][data-id='delete'][data-key='endpoint'] \
                      a[data-key='try-link'][href='/api/users/2']")
    LOCATOR_REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, "[data-http='post'][data-id='register-successful'][data-key='endpoint'] \
                                   a[data-key='try-link'][href='/api/register']")
    LOCATOR_REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, "[data-http='post'][data-id='register-unsuccessful'][data-key='endpoint'] \
                                     a[data-key='try-link'][href='/api/register']")
    LOCATOR_LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, "[data-http='post'][data-id='login-successful'][data-key='endpoint'] \
                                a[data-key='try-link'][href='/api/login']")
    LOCATOR_LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, "[data-http='post'][data-id='login-unsuccessful'][data-key='endpoint'] \
                                  a[data-key='try-link'][href='/api/login']")
    LOCATOR_LIST_USERS_DELAY = (By.CSS_SELECTOR, "[data-http='get'][data-id='delay'][data-key='endpoint'] \
                                a[data-key='try-link'][href='/api/users?delay=3']")
    LOCATOR_SPINNER = (By.CSS_SELECTOR, "[data-key='spinner']")
    LOCATOR_REQUEST = (By.CSS_SELECTOR, "span.url[data-key='url']")
    LOCATOR_REQUEST_BODY = (By.CSS_SELECTOR, "[data-key='output-request']")
    LOCATOR_RESPONSE_CODE = (By.CSS_SELECTOR, 'span.response-code')
    LOCATOR_RESPONSE_BODY = (By.CSS_SELECTOR, "pre[data-key='output-response']")
    RESPONSE_JSON_PARSED = (By.CSS_SELECTOR, 'body')


class ReqresBase(ReqresFrontBase):

    def find_list_examples(self):
        find_list = self.find_elements(ReqresLocator.LOCATOR_EXAMPLES_LIST)
        return find_list

    def find_request(self):
        find_request = self.find_element(ReqresLocator.LOCATOR_REQUEST)
        return find_request

    def find_response_code(self):
        find_response_code = self.find_element(ReqresLocator.LOCATOR_RESPONSE_CODE)
        return find_response_code

    def find_response_body(self):
        find_response_body = self.find_element(ReqresLocator.LOCATOR_RESPONSE_BODY)
        return find_response_body

    def find_invisible_response_body(self):
        spinner = self.find_element_wait_visible(ReqresLocator.LOCATOR_SPINNER)
        if spinner is None:
            return None
        find_response_body = self.find_element(ReqresLocator.LOCATOR_RESPONSE_BODY)
        return find_response_body

    def find_request_body(self):
        find_response_json_parsed = self.find_element(ReqresLocator.LOCATOR_REQUEST_BODY)
        return find_response_json_parsed

    def click_list_users(self):
        return self.click_element(ReqresLocator.LOCATOR_LIST_USERS)

    def click_single_user(self):
        return self.click_element(ReqresLocator.LOCATOR_SINGLE_USER)

    def click_single_user_not_found(self):
        return self.click_element(ReqresLocator.LOCATOR_SINGLE_USER_NOT_FOUND)

    def click_list_resource(self):
        return self.click_element(ReqresLocator.LOCATOR_LIST_RESOURCE)

    def click_single_resource(self):
        return self.click_element(ReqresLocator.LOCATOR_SINGLE_RESOURCE)

    def click_single_resource_not_found(self):
        return self.click_element(ReqresLocator.LOCATOR_SINGLE_RESOURCE_NOT_FOUND)

    def click_create(self):
        return self.click_element(ReqresLocator.LOCATOR_CREATE)

    def click_update_put(self):
        return self.click_element(ReqresLocator.LOCATOR_UPDATE_PUT)

    def click_update_patch(self):
        return self.click_element(ReqresLocator.LOCATOR_UPDATE_PATCH)

    def click_delete(self):
        return self.click_element(ReqresLocator.LOCATOR_DELETE)

    def click_register_successful(self):
        return self.click_element(ReqresLocator.LOCATOR_REGISTER_SUCCESSFUL)

    def click_register_unsuccessful(self):
        return self.click_element(ReqresLocator.LOCATOR_REGISTER_UNSUCCESSFUL)

    def click_login_successful(self):
        return self.click_element(ReqresLocator.LOCATOR_LOGIN_SUCCESSFUL)

    def click_login_unsuccessful(self):
        return self.click_element(ReqresLocator.LOCATOR_LOGIN_UNSUCCESSFUL)

    def click_list_users_delay(self):
        return self.click_element(ReqresLocator.LOCATOR_LIST_USERS_DELAY)
