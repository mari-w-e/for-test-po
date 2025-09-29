import json
import datetime
from tabulate import tabulate

# Создаем пустую коллекцию товаров
products = []

# Функция для добавления товаров
def add_product():
    category = input("Введите категорию товара: ")
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    price = correct_price(price)
    date = input("Введите дату покупки (дд-мм-гггг): ")
    date = correct_date(date)

    product = {"category": category, "name": name, "price": price, "date": date}

    products.append(product)
    save_to_file(products)

current_date = datetime.datetime.now().strftime('%d-%m-%Y')
ar_cur_date = list(map(int, current_date.split('-')))

def correct_date(date):
    while (date.count('-') != 2):
        date = input('Ошибка при вводе. Введите дату в формате дд-мм-гггг ')
    elem_date = list(map(int, date.split('-')))

    while not (0 < elem_date[0] < 32) or not (0 < elem_date[1] < 13) or not (2000 < elem_date[2] < 2025) or\
            (date.count('-') != 2) or ar_cur_date[2] < elem_date[2] or \
        (ar_cur_date[1] < elem_date[1] and ar_cur_date[2] == elem_date[2]) or \
        (ar_cur_date[0] < elem_date[0] and ar_cur_date[1] == elem_date[1] and ar_cur_date[2] == elem_date[2]):

        date = input('Недопустимое значение для даты. Введите корректную дату в формате дд-мм-гггг ')

        if ar_cur_date[2] < elem_date[2]:
            date = input('Недопустимое значение для даты. Введите корректную дату в формате дд-мм-гггг ')
        elif ar_cur_date[1] < elem_date[1]:
            date = input('Недопустимое значение для даты. Введите корректную дату в формате дд-мм-гггг ')
        elif ar_cur_date[0] < elem_date[0]:
            date = input('Недопустимое значение для даты. Введите корректную дату в формате дд-мм-гггг ')

        if date.count('-') != 2:
            while (date.count('-') != 2):
                date = input('Введите дату в формате дд-мм-гггг ')
                elem_date = list(map(int, date.split('-')))

        elem_date = list(map(int, date.split('-')))

    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (elem_date[0] > year[elem_date[1] - 1]):
        while (elem_date[0] > year[elem_date[1] - 1]) or (not (0 < elem_date[0] < 32) or \
                                not (0 < elem_date[1] < 13) or not (2020 < elem_date[2] < 2025)):
            date = input('Недопустимое значение для даты. Введите корректную дату в формате дд-мм-гггг ')
            if date.count('-') != 2:
                while (date.count('-') != 2):
                    date = input('Введите дату в формате дд-мм-гггг ')
                    elem_date = list(map(int, date.split('-')))
            elem_date = list(map(int, date.split('-')))

    elem_date = list(map(str, elem_date))
    if len(elem_date[0]) < 2:
        elem_date[0] = '0' + elem_date[0]
    if len(elem_date[1]) < 2:
        elem_date[1] = '0' + elem_date[1]
    return '-'.join(elem_date)



def is_number(str):
    try:
        float(str)
        return True
    except:
        return False


def correct_price(price):
    while not is_number(price):
        price = input('Недопустимое значение. Введите корректное значение цены ')
    price = round(float(price), 2)
    while not (0 < price < 10_000):
        price = input('Недопустимое значение. Введите корректное значение цены ')
        while not is_number(price):
            price = input('Недопустимое значение. Введите корректное значение цены ')
        price = round(float(price), 2)
    return(price)



# Функция для просмотра всех записанных товаров
def view_all_products():

    # преобразуем данные в список списков
    table_data = []
    for item in products:
        table_data.append([item['category'], item['name'], item['price'], item['date']])

    # вывод данных в виде таблицы
    print(tabulate(table_data, headers=['Категория', 'Название товара', 'Цена', 'Дата'], tablefmt="grid"))



# Функция для просмотра покупок по дате
def view_products_by_date():
    date = input("Введите дату (дд-мм-гггг): ")
    dates = []
    for product in products:
        dates.append(product['date'])
    while date not in dates:
        print('Проверьте корректность даты, введите повторно ')
        date = input("Введите дату (дд-мм-гггг): ")
    table_data = []
    for product in products:
        if product['date'] == date:

            # преобразуем данные в список списков
            table_data.append([product['category'], product['name'], product['price'], product['date']])

    # выводим данные в виде таблицы
    print(tabulate(table_data, headers=['Категория', 'Название товара', 'Цена', 'Дата'], tablefmt="grid"))



# Функция для просмотра покупок по категории
def view_products_by_category():
    category = input("Введите категорию: ")
    categories = []
    for product in products:
        categories.append(product['category'])
    while category not in categories:
        print('Нет добавленных товаров по введенной категории, проверьте категорию ')
        category = input("Введите категорию: ")

    table_data = []
    for product in products:
        if product['category'] == category:

            # преобразуем данные в список списков
            table_data.append([product['category'], product['name'], product['price'], product['date']])

    # выводим данные в виде таблицы
    print(tabulate(table_data, headers=['Категория', 'Название товара', 'Цена', 'Дата'], tablefmt="grid"))



# Функция для сортировки товаров по цене
def sort_products_by_price():
    orient_sort = input('Выберите направление сортировки (по возрастанию - 1 /по убыванию - 2) ')
    while orient_sort not in ['1', '2']:
        orient_sort = input('Некорректный ввод. ВВедите цифру. Выберите (по возрастанию - 1 /по убыванию - 2) ')
    if orient_sort == '1':
        sorted_products = sorted(products, key=lambda x: x['price'])
    elif orient_sort == '2':
        sorted_products = sorted(products, key=lambda x: x['price'], reverse=1)

    table_data = []
    for product in sorted_products:

        table_data.append([product['category'], product['name'], product['price'], product['date']])

    # выводим данные в виде таблицы
    print(tabulate(table_data, headers=['Категория', 'Название товара', 'Цена', 'Дата'], tablefmt="grid"))


# Функция для удаления записи о товаре
def delete_product():
    name = input("Введите название товара для удаления: ")
    products_to_delete = [product['name'] for product in products]
    while name not in products_to_delete:
        name = input("Товар не найден. Введите название товара для удаления повторно: ")
    for product in products:
        if product['name'] == name:
            products.remove(product)
            print('Товар успешно удален.')
    save_to_file(products)


# Функция для сохранения данных в файл
def save_to_file(data):
    with open("products.json", "w") as file:
        json.dump(data, file)


# Загрузка данных из файла, если файл существует
try:
    with open("products.json", "r") as file:
        products = json.load(file)
except FileNotFoundError:
    pass

# Основной цикл программы
if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Добавить товар")
        print("2. Просмотреть все товары")
        print("3. Просмотреть товары по дате")
        print("4. Просмотреть товары по категории")
        print("5. Сортировка товаров по цене")
        print("6. Удалить товар")
        print("7. Выход")
    
        choice = input("Выберите действие (1/2/3/4/5/6/7): ")
    
        if choice == "1":
            add_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            view_products_by_date()
        elif choice == "4":
            view_products_by_category()
        elif choice == "5":
            sort_products_by_price()
        elif choice == "6":
            delete_product()
        elif choice == "7":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
