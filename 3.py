# Введите элементы списка(числа) с клавиатуры, разделенные пробелами
user_input = input("Введите элементы списка через пробел: ")
if all(char.isdigit() or char.isspace() for char in user_input):
    input_list = user_input.split()
    my_list = []

# Преобразование элементов в список вещественных чисел
for item in input_list:
    my_list.append(float(item))
positive_sum = 0

for x in my_list:
    if x > 0:
        positive_sum += x
print("Сумма положительных элементов:", positive_sum)

index_of_zero = None
for i in range(len(my_list)):
    if my_list[i] == 0:
        index_of_zero = i
        break

if index_of_zero is not None:
    sum_after_zero = sum(my_list[index_of_zero + 1:])
    print("Сумма элементов после первого нуля:", sum_after_zero)
else:
    print("Сумму после первого нуля посчитать нельзя")


for x in my_list:
    if x < 0:
        my_list.remove(x)


print("Список после удаления отрицательных элементов:", my_list)
