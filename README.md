# Инструмент сравнения цен на MacBook в Алматы

Этот проект предоставляет простой инструмент для сравнения цен на модели MacBook в трех различных магазинах в Алматы: Alser, Sulpak и Technodom. Инструмент извлекает информацию из HTML-страниц продуктов каждого магазина, обрабатывает данные и создает несколько выходных файлов для анализа.

### Структура проекта:

- **sulpak.py:** Сбор данных с сайта Sulpak.
- **technodom.py:** Сбор данных с сайта Technodom.
- **Alser.py:** Сбор данных с сайта Alser.
- **meta_data.py:** Содержит URL и HEADER для выполнения запросов к веб-сайтам магазинов.
- **result_min_cost.csv:** Содержит информацию о минимальной стоимости каждого продукта в любом из магазинов.
- **result_max_count.csv:** Содержит информацию о магазине с максимальным количеством продуктов.
- **result_avg_price.csv:** Содержит информацию о средней цене продуктов в каждом магазине.
- **Alser_macbook_Almaty.csv, Sulpak_macbook_Almaty.csv, technodom_macbook_Almaty.csv:** Файлы с исходными данными, извлеченными из каждого магазина.
- **requirements.txt:** Содержит список установленных пакетов и их версий.

### Требования:

- **Python 3.x**
- **BeautifulSoup:** Для парсинга HTML-контента.
- **pandas:** Для манипуляции и анализа данных.
- **requests:** Для выполнения GET-запросов.

### Как использовать:

1. Установите необходимые пакеты с помощью следующей команды:

    ```bash
    pip install -r requirements.txt
    ```

2. Запустите скрипт `main.py`:

    ```bash
    python sulpak.py
    ```

3. Скрипт извлечет данные из указанных URL, обработает их и сгенерирует файлы с результатами.

### Файлы с результатами:

- **result_min_cost.csv:** Предоставляет информацию о минимальной стоимости каждого продукта в любом из магазинов.
- **result_max_count.csv:** Отображает магазин с максимальным количеством продуктов.
- **result_avg_price.csv:** Содержит информацию о средней цене продуктов в каждом магазине.

### Дополнительные замечания:

- Убедитесь, что необходимые библиотеки установлены перед запуском скрипта.
- Скрипт может потребовать обновления при изменениях в структуре веб-сайта.

### Автор:

Кумаров Нуржан

Сравнивайте цены с удовольствием!
