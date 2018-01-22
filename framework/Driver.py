from selenium import webdriver
import os


class Driver(object):
    """
    Base driver instance
    """
    @staticmethod
    def get_driver():
        driver = None
        if os.environ.get('SELENIUM_CONNECTION') == 'LOCAL':
            path = os.environ.get('SELENIUM_DRIVER_PATH')
            if os.environ.get('SELENIUM_BROWSER') == 'chrome':
                driver = webdriver.Chrome(executable_path=path)
            elif os.environ.get('SELENIUM_BROWSER') == 'firefox':
                driver = webdriver.Firefox(executable_path=path)
        elif os.environ.get('SELENIUM_CONNECTION') == 'REMOTE':
            driver = webdriver.Remote(
                command_executor=os.environ.get('SELENIUM_RC_URL'),
                desired_capabilities=os.environ.get('SELENIUM_BROWSER'))
        return Driver.add_driver_settings(driver)

    @staticmethod
    def add_driver_settings(driver):
        driver.set_page_load_timeout(20)
        driver.set_window_size(1280, 1024)
        return driver
