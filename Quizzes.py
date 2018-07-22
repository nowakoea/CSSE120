# Quiz 3

# def blah(x):
#     print(x * x)
#
#
# print(blah(5))
#
# size = 10
# for k in range(3):
#     size = size + 5
# size = size - 2
# print(size)
#
#
# def mystery(a, b):
#     c = a * b + a
#     return c
#
#
# mystery(4, 5)
# print('-----')
# print(mystery(4, 5))
# print('-----')
# print(mystery(7, 10))
#
#
# def mystery1(x, y):
#     x = 5
#     c = x * y
#     return c
#
#
# print(mystery1(8, 10))
# print('-----')
# x = 8
# y = 10
# print(mystery1(x, y))
# print('-----')
# print(x, y)


# Quiz 4
#
# def countEvens(n):
#     count = 0
#     for k in range(n):
#         if k % 2 == 0:
#             count = count + 1
#         print(k, count)
#     return count
#
#
# print(countEvens(4))

# Quiz 6

# for k in range(200, 215):
#     print(k)

# for k in range(100, 90 - 1, -1):
#     print(k)

# Quiz 10

# print('11' + str(3 + 3) + '22')
#
# x = 1
# y = 2
# z = 3
# print(str(x + y) + str(z))

x = []
for k in range(5):
    x = x + [(2 * k)]

print(x)

x = ()
for k in range(5):
    x = x + ((2 * k),)
print(x)

x = ''
for k in range(5):
    x = x + str(2 * k)
print(x)
