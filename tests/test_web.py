import pytest

from pages.top import TopPage
from pages.login import LogInPage

def test_Login(browser):
    # Given
    search_page = TopPage(browser)
    search_page.load()

    # When
    search_page.login_sign_up()

    # Verify that results appear
    login_page = LogInPage(browser)
    assert login_page.input_count() > 0
    assert login_page.enter_button_count() > 1
