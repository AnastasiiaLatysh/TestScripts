from framework.pages.BasePage import BasePage
from framework.elements.ContactUsElements import ContactsUsElements
from framework.Locators import ContactUsLocators


class ContactUsPage(BasePage):
    """
    Class which represents contact us page
    """

    def get_contact_us_elements(self):
        return ContactsUsElements(self.driver)

    def get_contact_us_title_text(self):
        return self.get_contact_us_elements().contact_us_title.text

    def enter_name(self, name):
        self.get_contact_us_elements().name_field.clear()
        self.get_contact_us_elements().name_field.send_keys(name)

    def enter_email(self, email):
        self.get_contact_us_elements().email_field.clear()
        self.get_contact_us_elements().email_field.send_keys(email)

    def enter_theme(self, theme):
        self.get_contact_us_elements().theme_field.clear()
        self.get_contact_us_elements().theme_field.send_keys(theme)

    def enter_description(self, description):
        self.get_contact_us_elements().description_field.clear()
        self.get_contact_us_elements().description_field.send_keys(description)

    def fill_contact_us_form(self, name, email, theme, question, description):
        self.enter_name(name)
        self.wait_until_element_to_be_filled(ContactUsLocators.NAME, name)
        self.enter_email(email)
        self.wait_until_element_to_be_filled(ContactUsLocators.EMAIL, email)
        self.enter_theme(theme)
        self.wait_until_element_to_be_filled(ContactUsLocators.THEME, theme)
        self.enter_description(description)
        self.get_contact_us_elements().questions_field.select_by_visible_text(question)
        self.wait_until_element_to_be_filled(ContactUsLocators.DESCRIPTION, description)

    def submit_contact_us_form(self):
        self.get_contact_us_elements().send_button.click()

    def is_contact_us_form_sent(self):
        self.wait_until_element_to_be_visible(ContactUsLocators.SUCCESSFUL_MESSAGE)
        return self.get_contact_us_elements().successful_message

    def get_success_message_text(self):
        return self.get_contact_us_elements().successful_message.text
