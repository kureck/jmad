from django.test import LiveServerTestCase
from selenium import webdriver


# https://codeyarns.com/2016/10/18/selenium-error-on-geckodriver/
class StudentTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_student_find_solos(self):
        """
        Test that a user can search for solos
        """
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
        self.assertEqual('JMAD', brand_element.text)
        self.fail('Incomplet test')
