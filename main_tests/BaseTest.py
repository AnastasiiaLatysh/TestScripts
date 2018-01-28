import unittest
from framework.Driver import Driver
from framework.pages.HomePage import HomePage
from framework.TestData import TestData, BASE_URL


class BaseTest(unittest.TestCase):

    general_data = TestData().load_general_data()
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()
        cls.home_page = HomePage(cls.driver, BASE_URL)
        cls.home_page.open()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
