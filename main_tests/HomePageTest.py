import unittest
from main_tests.BaseTest import BaseTest


class HomePageTest(BaseTest):

    def test_check_title(self):
        string_to_compare = self.general_data["page_title"]
        self.assertEqual(string_to_compare, self.home_page.get_title(), "Title is correct")

    def test_check_header_presence(self):
        self.assertTrue(self.home_page.get_base_elements().header.is_displayed(), "Header is displayed")

    def test_check_site_options(self):
        site_options_links = [self.general_data["header_elements"]["site_options"]["home_href"],
                              self.general_data["header_elements"]["site_options"]["contact_us_href"],
                              self.general_data["header_elements"]["site_options"]["site_map_href"]]
        for option_position in range(len(site_options_links)):
            self.assertEqual(site_options_links[option_position], self.home_page.get_site_options_links()[option_position],
                             "Link is correct for %d site option" % option_position)

    def test_check_scrolling(self):
        # check scrolling down
        position_before = self.home_page.get_scrolling_position()
        self.home_page.scroll_page()
        self.assertTrue(self.home_page.get_scrolling_position() > position_before, 'Scrolling down is executed')

        # check scrolling up
        position_before = self.home_page.get_scrolling_position()
        self.home_page.scroll_page(height_position=0)
        self.assertTrue(self.home_page.get_scrolling_position() < position_before, 'Scrolling up is executed.')
        self.assertEqual(0, self.home_page.get_scrolling_position(), 'Scrolling up is executed correctly.vv..')


if __name__ == "__main__":
    unittest.main()
