import os
import pathlib
import unittest
from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_example_page(self):
        self.driver.get(file_uri('example_page.html'))
        title = self.driver.title
        self.assertEqual(title, 'Example Page')

    def test_another_page(self):
        self.driver.get(file_uri('another_page.html'))
        header = self.driver.find_element_by_tag_name('h1').text
        self.assertEqual(header, 'Welcome to Another Page')