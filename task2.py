a = int(input('Введите число: '))

list = [1]

for i in range(a-1):
    list.append(list[i] * (i+2))
print(list)