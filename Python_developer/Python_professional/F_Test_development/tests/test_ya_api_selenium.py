import unittest
from selenium import webdriver
from time import sleep
from Python_developer.Python_professional.F_Test_development.config import EMAIL, PASS


class YaPassportSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_authorization(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element(by='css selector', value='div.AuthLoginInputToggle-type')
        elem.click()
        elem = driver.find_element(by='id', value='passp-field-login')
        elem.send_keys(EMAIL)
        elem = driver.find_element(by='id', value='passp:sign-in')
        elem.click()
        elem = driver.find_element(by='id', value='passp-field-passwd')
        elem.send_keys(PASS)
        elem = driver.find_element(by='id', value='passp:sign-in')
        elem.click()
        sleep(5)
        assert 'No results found.' not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
