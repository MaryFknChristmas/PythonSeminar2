a = str(input('Введите число: '))
sum = 0
for i in a:
    if i.isdigit():
        sum = sum + int(i)
print(sum)