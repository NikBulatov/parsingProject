import json
from pprint import pprint
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.product_page import ProductPage

LOGIN_LINK = "https://scrapingclub.com/exercise/basic_login/"
PRODUCT_LINK = 'https://scrapingclub.com/exercise/list_infinite_scroll/'


def write_result(file_name: str, data):
    with open(f'{file_name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def test_guest_login(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()

    name = password = browser.find_element(By.TAG_NAME, 'code').text
    login_page.login_user(name, password)
    login_page.should_be_success_message()

    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()

    product_page.scroll_down()
    data = product_page.get_data()

    pprint(data)
    write_result('result', data)
