import requests
import csv
from bs4 import BeautifulSoup
from meta_data import URLS, HEADER

response = requests.get(URLS['Alser'], headers=HEADER)
soup = BeautifulSoup(response.text, 'html.parser')


def info_technodom() -> object:
    quotes = soup.find_all('div', class_='card relative hover-shadow')

    with open(f'Alser_macbook_Almaty.csv', 'a', newline='', encoding='utf-8') as file:
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
            shop = 'Alser'
            card_title_elem = quot.find_all('div', class_='card__title body-small grey-text text-2-line')

            card_title = ' '.join([elem.text.strip() for elem in card_title_elem])

            card_def_price_elem = quot.find('div', class_="card__price")
            if card_def_price_elem:
                card_def_price = card_def_price_elem.text.strip()
            else:
                continue

            card_credit_price_elem = quot.find('div', class_='card__installment orange-text')
            if card_credit_price_elem:
                card_credit_price = card_credit_price_elem.text.strip()
            else:
                continue

            card_discount_elem = quot.find('div', class_='stickers__sticker body-small')
            percent_price = card_discount_elem.text.strip() if card_discount_elem else 'Без скидки'

            card_old_price_elem = quot.find('div', class_='card__old-price grey-text')
            old_price = card_old_price_elem.text.strip() if card_old_price_elem else 'Цена без скидки не указана'

            writer.writerow(
                (
                    shop,
                    card_title,
                    old_price,
                    card_def_price,
                    percent_price,
                    card_credit_price
                )
            )

    print(f'Данные успешно добавлены в файл Alser_macbook_Almaty.csv')


def main():
    info_technodom()


if __name__ == '__main__':
    main()
