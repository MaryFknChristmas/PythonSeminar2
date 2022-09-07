a = int(input('Введите число: '))

list = list(range(-a,a))
print(list)

numberOne = int(input('Введите позицию первого элемента: '))
numberTwo = int(input('Введите позицию второго элемента: '))

print(list[numberOne-1] * list[numberTwo-1])