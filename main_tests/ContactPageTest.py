import unittest
from main_tests.BaseTest import BaseTest
from framework.pages.HomePage import HomePage
from framework.TestData import TestData


class ContactPageTest(BaseTest):

    contact_us_data = TestData().load_contact_us_data()

    @classmethod
    def setUpClass(cls):
        super(ContactPageTest, cls).setUpClass()
        cls.home_page = HomePage(cls.driver)
        cls.contact_us_page = cls.home_page.open_contact_us_page()

    def test_check_url(self):
        self.assertEqual(self.general_data["page_urls"]["contact_us_page"], self.home_page.get_url(), "Url is correct")

    def test_check_contact_us_form(self):
        self.assertEqual(self.contact_us_data["contacts_us_page"]["title"],
                         self.contact_us_page.get_contact_us_title_text(), "Title is correct")

    # def test_send_contact_us_form(self):
    #     self.contact_us_page.fill_contact_us_form(
    #         self.contact_us_data["contacts_us_page"]["fromFields"]["name"],
    #         self.contact_us_data["contacts_us_page"]["fromFields"]["email"],
    #         self.contact_us_data["contacts_us_page"]["fromFields"]["theme"],
    #         self.contact_us_data["contacts_us_page"]["fromFields"]["questions"]["presscenter"],
    #         self.contact_us_data["contacts_us_page"]["fromFields"]["description"])
    #     self.contact_us_page.submit_contact_us_form()
    #     self.assertTrue(self.contact_us_page.is_contact_us_form_sent(), 'Contact form is sent')
    #     self.assertEqual(self.contact_us_data["contacts_us_page"]["successMessage"],
    #                      self.contact_us_page.get_success_message_text(), 'Successful message is correct')

if __name__ == "__main__":
    unittest.main()
