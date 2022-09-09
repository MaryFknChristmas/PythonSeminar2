a = input('Введите строку: ')
b = input('Введите вторую строку: ')
count = 0
i = 0

while i < len(a):
    if a[i : i+3] == b:
        count = count + 1
        i = i + 1
    else:
        i = i + 1

print(f'Количество вхождений второй строки в первую равно: {count}')
