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

# x = []
# for k in range(5):
#     x = x + [(2 * k)]
#
# print(x)
#
# x = ()
# for k in range(5):
#     x = x + ((2 * k),)
# print(x)
#
# x = ''
# for k in range(5):
#     x = x + str(2 * k)
# print(x)

# nums = 0
# for k in range(5):
#     nums = nums + (k * 2)
# print(nums)

# seq = [[1, 2, 3], [4, 5], [6], [7, 8, 9], []]
# for k in range(len(seq) - 1, -1, -1):
#     print(len(seq[k]))

# class SecretAgent(object):
#     def __init__(self, names):
#         self.names = names
#         self.current_name_index = 0
#
#     def show_all_names(self):
#         for k in range(len(self.names)):
#             print(self.names[k])
#
#     def change_to_next_name(self):
#         self.current_name_index = self.current_name_index + 1
#         if self.current_name_index > len(self.names):
#             self.current_name_index = 0
#
#     def give_current_name(self):
#         return self.names[self.current_name_index]
#
#
# agent1 = SecretAgent(['Mary', 'Jane', 'Lola', 'Terri'])
# agent2 = SecretAgent(['Bob', 'Niko', 'Rick', 'Zane', 'Alec'])
# agent1.change_to_next_name()
# print(agent1.give_current_name())
# print(agent2.give_current_name())

# Quiz 12

# def mystery(s):
#     for k in range(1, len(s)):
#         print(s[k - 1], s[k])
#
#
# mystery('csse120')

# Quiz 13

# for j in range(4):
#     for k in range(j):
#         print(j, k)

# Quiz 14

# def mystery_point(word):
#     for j in range(len(word)):
#         for k in range(j):
#             print('_', end='')
#         print(word[j])
#
#
# mystery_point('hello')

# def own_line(strings):
#     for j in range(len(strings)):
#         sublist = strings[j]
#         for k in range(len(strings[j])):
#             print(sublist[k])
#
#
# own_line('hello')

# import rosegraphics as rg
#
#
# def myster_draw(m, n, window):
#     x = 10
#     y = 20
#     for j in range(m):
#         for k in range(n):
#             upper_left = rg.Point(x, y)
#             lower_right = rg.Point(x + 20, y + 20)
#             rect = rg.Rectangle(upper_left, lower_right)
#             rect.attach_to(window)
#             window.render()
#             x = x + 20
#         x = 10
#         y = y + 20
#     window.close_on_mouse_click()


myster_draw(3, 5, rg.RoseWindow(400, 400))
