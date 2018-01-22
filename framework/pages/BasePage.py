from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from framework.elements.BaseElements import BaseElements
from selenium.webdriver.support import expected_conditions as EC
from framework.TestData import BASE_URL


class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver, base_url=BASE_URL):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)

    def get_title(self):
        return self.driver.title.strip()

    def get_url(self):
        return self.driver.current_url

    def get_base_elements(self):
        return BaseElements(self.driver)

    def get_site_options_links(self):
        links = []
        for site_option in self.get_base_elements().site_options:
            links.append(site_option.get_attribute('href'))
        return links

    def scroll_page(self, height_position='end'):
        """
        Method which scroll page to given height coordinates
        if height_position is not set, scrolling is executed till the end of page
        :param height_position: get int which refers to height coordinates of page to which scrolling should be executed
        :return: None
        """
        if height_position != 'end':
            self.driver.execute_script("window.scrollTo(0," + str(height_position) + ");")
        else:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_scrolling_position(self):
        return self.driver.execute_script("return window.pageYOffset;")

    def wait_until_element_to_be_filled(self, locator, text, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, text))
        except TimeoutException:
            raise AssertionError('It takes more than {} sec to fill element with text {}'.format(timeout, text))

    def wait_until_element_to_be_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError('It takes more than {} sec to load an element'.format(timeout))
