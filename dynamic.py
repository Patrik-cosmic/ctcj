# num = 10
# print(type(num))
# print(num)

# num = 25.36
# print(type(num))
# print(num)

# num = 'Suman'
# print(type(num))
# print(num)

# num = True
# print(type(num))
# print(num)
# import ctypes
# import sys

# num = 10
# temp = num
# print(id(num))

# print(ctypes.c_long.from_address(id(num)).value)
# print(ctypes.c_long.from_address(id(int(67))).value)
# num = 10
# print(id(num))
# print(num)

# num = num + 5
# print(id(num))
# print(num)

# num = 20
# print(id(num))
# print(num)

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

cont1 = [1, True, 2000, 200.56, [1, 2, 5]]
cont2 = [True, 23, 23.65, 'Suman', cont1]
        # [True, 23, 23.65, 'Suman', [1, True, 2000, 200.56, [1, 2, 5] ]
        
# print(id(cont2))
# print(cont2)
# print(cont2[4][1])
# print(type(cont2[4][1]))
# print(cont2[4][4][1])