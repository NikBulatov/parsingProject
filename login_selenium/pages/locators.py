from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.TAG_NAME, 'form')
    NAME_FIELD = (By.ID, 'id_name')
    PASSWORD_FIELD = (By.ID, 'id_password')
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_SUCCESS_MESSAGE = (
        By.XPATH, '//p[contains(text(), "Congratulations")]')


class ProductPageLocators:
    CARD = (By.XPATH, '//div[@class="card"]')
    CARD_TITLE = (By.XPATH, './/div[@class="card-body"]/h4/a')
    CARD_LINK = (By.XPATH, './/a')
    CARD_PRICE = (By.XPATH, './/div[@class="card-body"]/h5')
    CARD_IMAGE = (By.XPATH, './/a/img')
