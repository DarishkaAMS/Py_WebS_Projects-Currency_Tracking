import requests
from bs4 import BeautifulSoup
import time


class Currency:
    USD_UAH = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%B4%D0%BE+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%96&oq=%D0%BA%D1%83%D1%80&aqs=chrome.0.69i59j69i57j35i39j69i59j0j69i61l3.1353j0j7&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    current_converted_price = 0
    difference = 0.1

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(USD_UAH, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price())
        if currency >= self.current_converted_price + self.difference:
            print("The exchange range has grown a lot! Go and do something")
        elif currency <= self.current_converted_price - self.difference:
            print("The exchange range has dropped a lot! Go and do something")
        print("At the moment 1 USD = ", currency)
        time.sleep(3)
        check_currency()

