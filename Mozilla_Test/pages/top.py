from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TopPage:
    # URL
    URL = 'https://people.mozilla.org/'

    # ELEMENTs
    SEARCH_INPUT = (By.CSS_SELECTOR, '.home__button-link ')
    SEARCH_BUTTON = (By.CLASS_NAME, 'search-form__submit')
    BTN_ID = (By.ID, 'search-query')
    TOGGLE = (By.ID, 'search-who-form')
    LEARNMORE = (By.XPATH, "//a[@target='_blank']")
    WIKI_H1 = (By.ID, 'firstHeading')
    GETINVOLVED = (By.XPATH, '//*[@id="app"]/main/section/a')
    CARD_IMG = (By.CLASS_NAME, 'mzp-c-card-image')

    # METHOD
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    # Action
    def login_sign_up(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(Keys.RETURN)

    def click_search_box(self):
        search_search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_search_button.click()

    def click_learnmore(self):
        search_learnmore = self.browser.find_element(*self.LEARNMORE)
        search_learnmore.click()

    def switch_to_wiki(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def click_getinvolved(self):
        search_getinvolved = self.browser.find_element(*self.GETINVOLVED)
        search_getinvolved.click()

    # Find Elements
    def enter_button_count(self):
        btn_cnt = self.browser.find_elements(*self.BTN_ID)
        return len(btn_cnt)

    def toggle_count(self):
        toggle_cnt = self.browser.find_elements(*self.TOGGLE)
        return len(toggle_cnt)

    def wiki_count(self):
        wiki_cnt = self.browser.find_elements(*self.WIKI_H1)
        return len(wiki_cnt)

    def cardimg_count(self):
        cardimg_cnt = self.browser.find_elements(*self.CARD_IMG)
        return len(cardimg_cnt)