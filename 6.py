import random
while True:
    try :
        length = input("Введите длину кортежа")
        length = int(length)
        break
    except ValueError:
        print("Некорректный ввод, попробуйте ещё раз")

tuple = tuple(random.randint(1, 100) for _ in range(length))
print(tuple)
print(tuple[0],tuple[-1])
