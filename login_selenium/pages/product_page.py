import time

from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def scroll_down(self):
        pause_time = 2.5
        body_height = self.browser.execute_script(
            "return document.body.scrollHeight")
        while True:
            self.browser.execute_script(f'window.scrollTo(0, {body_height});')
            time.sleep(pause_time)
            new_height = self.browser.execute_script(
                'return document.body.scrollHeight')
            if new_height == body_height:
                break
            body_height = new_height

    def get_data(self):
        cards = self.browser.find_elements(*ProductPageLocators.CARD)
        data = []
        for card in cards:
            title = card.find_element(
                *ProductPageLocators.CARD_TITLE).text
            price = card.find_element(
                *ProductPageLocators.CARD_PRICE).text
            link = card.find_element(
                *ProductPageLocators.CARD_LINK).get_attribute('href')
            image = card.find_element(
                *ProductPageLocators.CARD_IMAGE).get_attribute('src')
            data.append({'title': title,
                         'price': price,
                         'link': link,
                         'image': image})
        return data
