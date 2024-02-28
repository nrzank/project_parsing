import requests
import csv
from bs4 import BeautifulSoup
from meta_data import URLS, HEADER

response = requests.get(URLS['Technodom'], headers=HEADER)
soup = BeautifulSoup(response.text, 'html.parser')


def info_technodom() -> object:

    quotes = soup.find_all('div', class_="ProductCardV_card__xHsl_ ProductItem_product__hZy7p")

    with open(f'technodom_macbook_Almaty.csv', 'a', newline='', encoding='utf-8') as file:
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
            shop = 'Technodom'
            card_title_elem = quot.find('div', class_="ProductCardV_titleWrapper__x5c25")
            if card_title_elem:
                card_title = card_title_elem.text.strip()
            else:
                continue

            card_def_price_elem = quot.find('p', class_="Typography ProductCardPrices_price__oCsLy Typography__Subtitle")
            if card_def_price_elem:
                card_def_price = card_def_price_elem.text.strip()
            else:
                continue

            card_credit_price_elem = quot.find('div', class_='ProductCardCreditTerms_creditTerms__LaVNO')
            if card_credit_price_elem:
                card_credit_price = card_credit_price_elem.text.strip()
            else:
                continue

            card_discount_elem = quot.find('p', class_='Typography StickerNext StickerNext__Text ProductCardTopStickers_sticker__CKC_P Typography__Caption Typography__Caption_Bold')
            percent_price = card_discount_elem.text.strip() if card_discount_elem else 'Без скидки'

            card_old_price_elem = quot.find('p', class_='Typography ProductCardPrices_oldPrice__wokOV Typography__Caption Typography__Caption_Strikethrough')
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

    print(f'Данные успешно добавлены в файл technodom_macbook_Almaty.csv')


def main():
    info_technodom()


if __name__ == '__main__':
    main()
