import requests
import csv
from bs4 import BeautifulSoup
from meta_data import URLS, HEADER

response = requests.get(URLS['Sulpak'], headers=HEADER)
soup = BeautifulSoup(response.text, 'html.parser')


def info_sulpak():
    quotes = soup.find_all('div', class_="product__item-inner")

    with open(f'Sulpak_macbook_Almaty.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Имя магазина',
                'Название модели',
                'Старая цена',
                'Новая цена',
                'Процент скидки',
                'В кредит'
            )
        )
        for quot in quotes:
            shop = 'Sulpak'
            card_title_elem = quot.find('div', class_="product__item-name")

            if card_title_elem:
                card_title = card_title_elem.text.strip()
            else:
                continue

            card_def_price_elem = quot.find('div', class_="product__item-price")
            if card_def_price_elem:
                card_def_price = card_def_price_elem.text.strip()
            else:
                continue

            card_discount_elem = quot.find('div', class_='product__label-discount')
            percent_price = card_discount_elem.text.strip() if card_discount_elem else 'Без скидки'

            card_old_price_elem = quot.find('div', class_='product__item-price-old super-price')
            old_price = card_old_price_elem.text.strip() if card_old_price_elem else 'Цена без скидки не указана'

            writer.writerow(
                (
                    shop,
                    card_title,
                    old_price,
                    card_def_price,
                    percent_price,
                    'Нет данных'
                )
            )
    print(f'Файл Sulpak_macbook_Almaty.csv успешно записан')


def main():
    info_sulpak()


if __name__ == '__main__':
    main()


