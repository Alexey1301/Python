my_dict = {
    'яблоко': 5,
    'банан': 2,
    'груша': 7,
    'апельсин': 3,
    'манго': 1
}
# # Создаем пустой словарь
# my_dict = {}
# # Запускаем цикл для ввода данных с клавиатуры
# while True:
#     key = input("Введите ключ (или 'q' для завершения): ")
#     # Проверяем, если пользователь ввел 'q', то завершаем цикл
#     if key == 'q':
#         break
#     value = input("Введите значение: ")
#     # Добавляем введенную пару ключ-значение в словарь
#     my_dict[key] = value
# # Выводим заполненный словарь
# print("Заполненный словарь:")
# for key, value in my_dict.items():
#     print(f'{key}: {value}')

sorted_dict = dict(sorted(my_dict.items(),key= lambda x:x[1]))
print(sorted_dict)
