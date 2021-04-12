from selenium.webdriver.common.by import By


class LogInPage(object):
    LINK_DIVS = (By.ID, 'field-email')
    SEARCH_INPUT = (By.ID, 'field-email')

    # @classmethod
    # def PHRASE_RESULTS(cls, phrase):
    #     xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
    #     return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def input_count(self):
        inputs = self.browser.find_elements(*self.LINK_DIVS)
        return len(inputs)


    # def phrase_result_count(self, phrase):
    #     phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
    #     return len(phrase_results)

    # def search_input_value(self):
    #     search_input = self.browser.find_element(*self.SEARCH_INPUT)
    #     return search_input.get_attribute('value')