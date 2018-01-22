import os
import json
import codecs

PATH_TO_GENERAL_DATA = os.path.abspath('') + '/testing_data.json'
PATH_TO_CONTACT_US_DATA = os.path.abspath('') + '/contact_us_data.json'
BASE_URL = os.environ.get('BASE_URL')


class TestData(object):
    """
    Class which returns data from json for testing specified page
    """

    @staticmethod
    def load_general_data():
        with codecs.open(PATH_TO_GENERAL_DATA, encoding='utf-8') as general_data:
            return json.loads(general_data.read())

    @staticmethod
    def load_contact_us_data():
        with codecs.open(PATH_TO_CONTACT_US_DATA, encoding='utf-8') as contact_us_data:
            return json.loads(contact_us_data.read())
