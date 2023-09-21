while True:
    s = input("Введите строку:")
    if(s.isalpha()):
        break
    else:
        print("Некорректный ввод, попробуйте ещё раз")

# s = input("Введите строку")
pairs_count = i = vowel_count = 0

for i in range(1,len(s)):
    if (s[i-1].isupper() and s[i].isupper()) or (s[i-1].islower() and s[i].islower()) :
        pairs_count += 1
    if s[i] in  'aeyuioAEYUIO':
        vowel_count += 1
print("Количество пар верхнего и нижнего регистра:", pairs_count)
print("Количество гласных букв:" , vowel_count)
