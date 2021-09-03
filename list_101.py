# List container type 

# cont = list()

# cont = [True, 23, 23.65, 'Suman']
# print(id(cont))
# print(cont)

# cont.append('CTCJ')
# print(id(cont))
# print(cont)

# cont.append(20)
# print(id(cont))
# print(cont)

# print(type(cont))
# print(cont[0])
# print(type(cont[0]))
# print(type(cont[2]))
# print(type(cont[3]))

# numbers = 10, 12, 14, 16
# numbers = (10, 12, 14, 16)
# print(type(numbers))
# print(numbers)

# numbers = (10, 12.56, True, 'Tithi')
# print(type(numbers))
# print(numbers)
# print(numbers[2])
# print(type(numbers[2]))

# cont1 = [1, True, 2000, 200.56, [1, 2, 5]]
# cont2 = [True, 23, 23.65, 'Suman', cont1]
#         # [True, 23, 23.65, 'Suman', [1, True, 2000, 200.56, [1, 2, 5] ]
    
# print(id(cont2))
# print(cont2)
# print(cont2[4][1])
# print(type(cont2[4][1]))
# print(cont2[4][4][1])

# cont1 = [
#     1,        # 0
#     True,     # 1
#     2000, 
#     200.56,
#     [1, 2, 5] # 4
#     # index of 1 would be => cont1[4][0]
#  ]


# numbers = [2, 4, 6, 8, 9]

# general form # for identifier(num) keyword(in) iterable(numbers):
# #       ...
 
# for num in numbers:
#     print(num)

# name = 'Suman De'

# for char in name:
#     print(char)

# numbers = range(10) # 0, 1, 2, 3, 4, 5,
# # print(type(numbers))
# print(numbers)
# 
# # number_list = list(numbers)
# # print(type(number_list))
# # print(number_list)
# 
# for i in range(10): # start = 0, stop = the number you gave, step = 1
#     print(i)
# 
# # 20 22 24 26 28 !30
# for i in range(20, 30, 2): # start = 0, stop = the number you gave, step = 1
#     print(i)
# 
# for i in range(20, 10, -2): # start = 0, stop = the number you gave, step = 1
#     print(i)

Shiva = 'Suman,Patrik,Wattson,Foo,Bar'.split(',')
#Suman*Patrik*
print(type(Shiva))
print(Shiva)
print(len(Shiva))


