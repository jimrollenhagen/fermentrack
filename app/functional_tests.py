from selenium import webdriver
import unittest


class NewInstallationTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_configure_fermentrack_and_add_controller(self):
        self.browser.get('http://localhost:8000')


        # The user launches a (presumably brand new) copy of Fermentrack and is asked to configure the software
        # The user sets the configuration options & saves them to the database
        # The user is presented with an empty "All Controllers" page
        self.assertIn('All Controllers', self.browser.title)

        self.fail('Finish the test')

        # The user navigates to the "Add Controller" workflow and adds a controller
        # The user now sees the controller on the "All Controller" screen


if __name__ == '__main__':
    unittest.main(warnings='ignore')
