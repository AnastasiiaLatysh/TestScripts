from framework.pages.BasePage import BasePage
from framework.pages.ContactUsPage import ContactUsPage


class HomePage(BasePage):
    """
    Class which represents general view of page
    """

    def open_contact_us_page(self):
        self.get_base_elements().contact_us_option.click()
        return ContactUsPage(self.driver)
