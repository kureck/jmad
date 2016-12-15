# from django.test import LiveServerTestCase
# from selenium import webdriver
#
#
# # https://codeyarns.com/2016/10/18/selenium-error-on-geckodriver/
# class StudentTestCase(LiveServerTestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(2)
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_student_find_solos(self):
#         """
#         Test that a user can search for solos
#         """
#         home_page = self.browser.get(self.live_server_url + '/')
#         brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
#         self.assertEqual('JMAD', brand_element.text)
#
#         instrument_input = self.browser.find_element_by_css_selector('input#jmad-instrument')
#         self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-instrument"]'))
#         self.assertEqual(instrument_input.get_attribute('placeholder'),'i.e. trumpet')
#
#         artist_input = self.browser.find_element_by_css_selector('input#jmad-artist')
#         self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-artist"]'))
#         self.assertEqual(artist_input.get_attribute('placeholder'), 'i.e. Davis')
#
#         instrument_input.send_keys('saxophone')
#         self.browser.find_element_by_css_selector('form button').click()
#
#         search_results = self.browser.find_elements_by_css_selector('.jmad-search-result')
#         self.assertGreater(len(search_results), 2)
#
#         second_artist_input = self.browser.find_element_by_css_selector('input#jmad-artist')
#         second_artist_input.send_keys('Cannonball Adderley')
#         self.browser.find_element_by_css_selector('form button').click()
#         second_search_results = self.browser.find_elements_by_css_selector('.jmad-search-result')
#         self.assertEqual(len(second_search_results), 2)
#         self.fail('Incomplet test')
