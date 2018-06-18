# Quiz 3

def blah(x):
    print(x * x)


print(blah(5))

size = 10
for k in range(3):
    size = size + 5
size = size - 2
print(size)


def mystery(a, b):
    c = a * b + a
    return c


mystery(4, 5)
print('-----')
print(mystery(4, 5))
print('-----')
print(mystery(7, 10))


def mystery1(x, y):
    x = 5
    c = x * y
    return c


print(mystery1(8, 10))
print('-----')
x = 8
y = 10
print(mystery1(x, y))
print('-----')
print(x, y)
