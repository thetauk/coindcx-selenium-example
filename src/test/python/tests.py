import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from tauk.tauk_webdriver import Tauk

from src.test.python.project_capabilities import ProjectCapabilities
from src.test.python.test_base import TestBase


class Tests(TestBase):

    def pre_launch(self):
        self.browser = 'chrome'
        self.caps = ProjectCapabilities.base_capabilities(self.browser)

    def setUp(self):
        super().setUp()
        Tauk(
            api_token="YOUR_API_TOKEN",
            project_id="YOUR_PROJECT_ID"
        )

    def tearDown(self):
        super().tearDown()

    @Tauk.observe(custom_test_name="test_CoinDCX_Explore")
    def test_CoinDCX_Explore(self):
        Tauk.register_driver(self.driver)
        self.driver.get("https://coindcx.com/")
        print("Clicking on the [Pro] Button")
        self.wait.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.pro-wrapper'))
        ).click()

        print("Clicking on the [Learn]")
        self.wait.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.learn-wrapper'))
        ).click()

        self.driver.get("https://coindcx.com/")

        print("Clicking on the [OTC]")
        self.wait.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.otc-wrapper'))
        ).click()


if __name__ == '__main__':
    unittest.main()
