a = list(range(1, 6))

print(a)

b = a.copy()

i = 0

while i < len(b)/2:
    temp = b[i]
    b[i] = b[i+1]
    b[i+1] = temp
    i += 1
else:
    temp = b[-1]
    b[-1] = b[0]
    b[0] = temp


print(b)