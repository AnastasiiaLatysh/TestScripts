from framework.Locators import HeaderLocators


class BaseElements(object):
    """
    Class which contains base elements which are displayed on all site's pages 
    """

    def __init__(self, driver):
        self.driver = driver

    @property
    def header(self):
        return self.driver.find_element(*HeaderLocators.HEADER)

    @property
    def site_options(self):
        return self.driver.find_elements(*HeaderLocators.SITE_OPTIONS)

    @property
    def home_option(self):
        return self.driver.find_element(*HeaderLocators.HOME_OPTION)

    @property
    def contact_us_option(self):
        return self.driver.find_element(*HeaderLocators.CONTACT_US_OPTION)
