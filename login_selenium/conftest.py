import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Edge()
    print("\nstart browser for test...")
    yield browser
    print("\nquit browser..")
    browser.quit()
