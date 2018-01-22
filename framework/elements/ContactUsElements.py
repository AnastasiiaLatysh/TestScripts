from framework.elements.BaseElements import BaseElements
from framework.Locators import ContactUsLocators
from selenium.webdriver.support.select import Select


class ContactsUsElements(BaseElements):
    """
    Class which contains elements which are displayed on Contacts us page
    """

    @property
    def contact_us_title(self):
        return self.driver.find_element(*ContactUsLocators.CONTACT_US_TITLE)

    @property
    def name_field(self):
        return self.driver.find_element(*ContactUsLocators.NAME)

    @property
    def email_field(self):
        return self.driver.find_element(*ContactUsLocators.EMAIL)

    @property
    def theme_field(self):
        return self.driver.find_element(*ContactUsLocators.THEME)

    @property
    def questions_field(self):
        return Select(self.driver.find_element(*ContactUsLocators.QUESTIONS))

    @property
    def description_field(self):
        return self.driver.find_element(*ContactUsLocators.DESCRIPTION)

    @property
    def send_button(self):
        return self.driver.find_element(*ContactUsLocators.SEND_BUTTON)

    @property
    def successful_message(self):
        return self.driver.find_element(*ContactUsLocators.SUCCESSFUL_MESSAGE)
