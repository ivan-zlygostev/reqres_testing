from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class ReqresFrontBase:
    def __init__(self, driver, host):
        self.driver = driver
        self.host = host

    def go_to_url(self):
        return self.driver.get(self.host)

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            element = None
        return element

    def find_element_wait_visible(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            element = None
            print('aaaaa')
        return element

    def find_elements(self, locator, time=10):
        try:
            elements = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                              message=f'Cant find elements by locator {locator}')
        except TimeoutException:
            elements = None
        return elements

    def check_element_clickable(self, locator, time=100000):
        try:
            element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                             message=f'Cant find elements by locator {locator}')
        except TimeoutException:
            element = None
        return element

    def scroll_shim(self, passed_in_driver, object):
        x = object.location['x']
        y = object.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        passed_in_driver.execute_script(scroll_by_coord)
        passed_in_driver.execute_script(scroll_nav_out_of_way)

    def click_element(self, locator):
        element = self.check_element_clickable(locator=locator)
        self.scroll_shim(passed_in_driver=self.driver, object=element)
        return element.click()
