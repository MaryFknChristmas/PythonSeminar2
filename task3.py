a = int(input('Введите число: '))
sum = 0
list = [2]
for i in range(a-1):
    list.append((1 + (1/(i+2)))**(i+2))
print(list)

for i in list:
    sum = sum+i
print(round((sum), 3))