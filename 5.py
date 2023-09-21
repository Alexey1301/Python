# Словарь с информацией о продукции
menu = {
    'торт': ['Шоколадный торт', 200, 500],
    'пирожное': ['Ванильное пирожное', 50, 200],
    'маффин': ['Голубика маффин', 80, 300],
    'печенье': ['Овсяное печенье', 40, 400],
    'шоколадка': ['Темный шоколад', 120, 150],
    'мороженое': ['Ванильное мороженое', 60, 1000]
}
def show_description(product):
    if product in menu:
        print(product - menu[product][0])
    else:
        print("Продукт не найден")

def show_price(product):
    if product in menu:
        print(product - menu[product][1], "рублей за 100 грамм")
    else:
        print("Продукт не найден")

def show_quantity(product):
    if product in menu:
        print(product - menu[product][2], "грамм")
    else:
        print("Продукт не найден")

def show_all_info():
    for product, info in menu.items():
        print(product, info[0], "Цена:", info[1], "рублей за 100 грамм, Количество:", info[2], "грамм")

# def make_purchase():
#     total_price = 0
#     while True:
#         product = input("Введите название продукции (или 'q' для завершения покупки): ").lower()
#         if product == 'q':
#             break
#         if product in menu:
#             quantity_input = input("Введите количество" ,menu[product][0], "грамм: ")
#             if quantity_input.isdigit():
#                 quantity = float(quantity_input)
#                 if quantity > menu[product][2]:
#                     print("Извините, недостаточно товара.")
#                 else:
#                     total_price += menu[product][1] * (quantity / 100)
#                     menu[product][2] -= quantity
#             else:
#                 print("Введите корректное количество.")
#         else:
#             print("Продукт не найден")
#
#     print("Общая стоимость покупки:" ,total_price, "рублей")
#     print("Остаток товаров:")
#     show_all_info()
def make_purchase():
    total_price = 0
    while True:
        product = input("Введите название продукции (или 'q' для завершения покупки): ").lower()
        if product == 'q':
            break
        if product in menu:
            try:
                quantity = float(input(f"Введите количество {menu[product][0]} (грамм): "))
                if quantity > menu[product][2]:
                    print("Извините, недостаточно товара.")
                else:
                    total_price += menu[product][1] * (quantity / 100)
                    menu[product][2] -= quantity
            except ValueError:
                print("Введите корректное количество.")
        else:
            print("Продукт не найден")

    print(f"Общая стоимость покупки: {total_price} рублей")
    print("Остаток товаров:")
    show_all_info()
while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        product = input("Введите название продукции: ").lower()
        show_description(product)
    elif choice == '2':
        product = input("Введите название продукции: ").lower()
        show_price(product)
    elif choice == '3':
        product = input("Введите название продукции: ").lower()
        show_quantity(product)
    elif choice == '4':
        show_all_info()
    elif choice == '5':
        make_purchase()
    elif choice == '6':
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите пункт из меню.")
