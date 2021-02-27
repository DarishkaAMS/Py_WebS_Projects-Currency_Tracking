import requests

from bs4 import BeautifulSoup

USD_UAH = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%B4%D0%BE+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%96&oq=%D0%BA%D1%83%D1%80&aqs=chrome.0.69i59j69i57j35i39j69i59j0j69i61l3.1353j0j7&sourceid=chrome&ie=UTF-8"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

full_page = requests.get(USD_UAH, headers)
print(full_page.content)
