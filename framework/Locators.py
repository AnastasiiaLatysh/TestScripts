from selenium.webdriver.common.by import By


class HeaderLocators(object):
    HEADER = (By.CSS_SELECTOR, "#bone > div.b-bar.clearfix")
    SITE_OPTIONS = (By.XPATH, "//ul[@class='site-services nm clearfix']/li/a")
    HOME_OPTION = (By.XPATH, "//ul[@class='site-services nm clearfix']/li[@id='home']")
    CONTACT_US_OPTION = (By.XPATH, "//*[@id='mail']")


class ContactUsLocators(object):
    CONTACT_US_TITLE = (By.XPATH, "//div[@class='article']/h1")
    NAME = (By.ID, "contact_form1")
    EMAIL = (By.ID, "contact_form2")
    THEME = (By.ID, "contact_form3")
    QUESTIONS = (By.ID, "contact_form4")
    DESCRIPTION = (By.ID, "contact_form5")
    SEND_BUTTON = (By.CSS_SELECTOR, "#id-button.send-btn")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "#error.b-positive.mess")
