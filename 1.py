while True:
    try:
        x = input("Введите число")
        x = int(x)
        break;
    except ValueError:
        print("Некорректный ввод, попробуйте ещё раз")
res = 'Yes'
while x>9:
    if (x%10) <= (x/10%10):
        res = 'NO'
    x = x // 10
print(res)