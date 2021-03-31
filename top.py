from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TopPage:
    URL = 'https://people.mozilla.org/'

    SEARCH_INPUT = (By.CSS_SELECTOR, '.home__button-link ')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login_sign_up(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(Keys.RETURN)