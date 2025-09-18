########################## 15.1 #####################
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     # def __add__(self, other):
#     #     rectang = self.get_square() + other.get_square()
#     #
#     #     new_width = self.width
#     #     new_height = rectang / new_width
#     #
#     #     return Rectangle(new_width, new_height)
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             square_new_rect = self.get_square() + other.get_square()
#             return Rectangle(self.width, square_new_rect / self.width)
#
#         raise NotImplementedError
#
#     def __eq__(self, other):
#         return self.get_square() == other.get_square()
#
#     def __mul__(self, n):
#         rectang = self.get_square() * n
#
#         new_width = self.width
#         new_height = rectang / new_width
#
#         return Rectangle(new_width, new_height)
#
#     def __str__(self):
#         return str(self.get_square())


############################# 15.2 #############################
# class Fraction:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __mul__(self, other):
#         return Fraction(self.a * other.a, self.b * other.b)
#
#     def __add__(self, other):
#         return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)
#
#     def __sub__(self, other):
#         return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)
#
#     def __eq__(self, other):
#         num_1 = self.a * other.b
#         num_2 = other.a * self.b
#
#         return num_1 == num_2
#
#     def __gt__(self, other):
#         num_1 = self.a * other.b
#         num_2 = other.a * self.b
#
#         return num_1 > num_2
#
#     def __lt__(self, other):
#         num_1 = self.a * other.b
#         num_2 = other.a * self.b
#
#         return num_1 < num_2
#
#     def __str__(self):
#         return f"Fraction: {self.a}, {self.b}"













# import csv
# import sqlite3
# import time
#
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
#
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
#     }
#
#
# def get_data(url: str) -> str:
#     service = Service("/Users/vova/hillel/pb_24-07/geckodriver")
#     worker = webdriver.Firefox(service=service)
#     worker.get(url)
#     time.sleep(3)
#     html = worker.page_source
#     worker.quit()
#     return html
#
# def parse_data(html: str) -> list:
#     rez = []
#     if html:
#         soup = BeautifulSoup(html, 'html.parser')
#         div_list = soup.find_all('div', attrs={'class': 'item'})
#         for div in div_list:
#             # Пошук тега а
#             a = div.find('a', attrs={'class': 'tile-image-host'})
#             # Беремо у тега а атрибут href
#             try:
#                 href = a['href']
#             except:
#                 continue
#             # За допомогою атрибуту текст, забираємо всю текстову
#             # інформацію, що міститься в цьому тегу
#             title = a['title']
#             old = div.find('div', attrs={'class': 'old-price'})
#             price = div.find('div', attrs={'class': 'price'})
#             # Стара ціна є не у всіх, тому потрібно зробити дефолтне значення
#             old_price = ''
#             if old:
#                 # Якщо контейнер із старою ціною є
#                 old = old.text
#                 # І в цьому контейнер є інфа
#                 if old:
#                     # Забираємо лише те, що є цифрами та формуємо значення ціни
#                     old_price = int(''.join(c for c in old if c.isdigit()))
#             # Звичайна ціна є скрізь, тому формуємо значення
#             price = int(''.join(c for c in price.text if c.isdigit()))
#             # Результат за кожною відеокартою записуємо у вигляді словника
#             rez.append(
#                 {
#                     'title': title,
#                     'href': href,
#                     'price': price,
#                     'old_price': old_price,
#                     }
#                 )
#     return rez
#
#
# def save_data(data: list[dict], filename: str) -> None:
#     column_names = data[0].keys()
#
#     with open(filename, "w", newline="", encoding="utf-8") as file:
#         writer = csv.DictWriter(file, fieldnames=column_names, delimiter=";")
#         writer.writeheader()
#         writer.writerows(data)
#
#
# def save_data_to_sqlite(data: list[dict], db_name: str) -> None:
#     with sqlite3.connect(db_name) as conn:
#         cursor = conn.cursor()
#         # cursor.execute('''DROP TABLE IF EXISTS video_cards''')
#         cursor.execute('''CREATE TABLE IF NOT EXISTS video_cards
#                           (title TEXT, href TEXT, price INTEGER, old_price INTEGER)''')
#         for item in data:
#             cursor.execute("INSERT INTO video_cards VALUES (?, ?, ?, ?)",
#                            (item['title'], item['href'], item['price'], item['old_price']))
#         conn.commit()
#
#
# def get_data_from_sqlite(db_name: str) -> list[dict]:
#     with sqlite3.connect(db_name) as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM video_cards where old_price == ''")
#         return list(cursor.fetchall())
#
#
# def main():
#     # url = "https://hard.rozetka.com.ua/ua/videocards/c80087/page={}"
#     # parsedata = []
#     # for i in range(1, 2):
#     #     html = get_data(url.format(i))
#     #     data = parse_data(html)
#     #     parsedata.extend(data)
#
#     # save_data(parsedata, "output.csv")
#     # save_data_to_sqlite(parsedata, "output.sqlite")
#     print(get_data_from_sqlite("output.sqlite"))
#
#
# if __name__ == "__main__":
#     main()