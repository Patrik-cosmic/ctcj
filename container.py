##### list

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print(type(numbers))
# print(numbers)

# result = numbers.append(9)
# result2 = numbers.count(3)
# removed_item = numbers.pop() # 8

# print(removed_item)
# print(numbers)


# print(numbers)
# print(result)
# print(result2)

##### tuple 
#days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')


# days_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# days_list.append('Spider man')
# # days.append('Spider')
# print(days_list)

# days = (
#     'sun', 
#     'mon', 
#     'Tue',
#     'Wed', 
#     'Thu', 
#     'Fri',
#     'Fri',
#     True,
#     [1, 2, 3, 4, 5, 6, 7, 8], # add number 9
#     (True, False, True)
# )

# days[8][4] = 99
# print(days)

# print(days.count('Fri'))
# position = days.index([1, 2, 3, 4, 5, 6, 7, 8])
# print(position)

# # print(days[7])
# # print(type(days[7]))

# days[7].append(9)

# print(days)
# print(days[7])

# set
# student_marks = [15, 15, 15, 15, 17, 17, 18]
# print(student_marks)

# # student_marks = {15, 15, 15, 15, 17, 17, 18, 19}
# student_marks = set(student_marks)
# print(student_marks)


# home task
# (10, 10, 45, 45, 87) => unique(45, 10, 87) => minimum(10)

# random_set = {
#     (10, 20, 30, 10), 
#     (10, 20, 30, 10), 
#     'Suman',
#     True, 
#     False, False, False
#  }

# print(id(random_set[0]))
# print(id(random_set[1]))
# print(random_set)

# temp = [
#      [1, 2, 30],
#      30,
#      20, 
#      True,
#      False, 
#      30, 
#      1
# ]

# print(temp[0][0] is temp[6])
# n = tuple([10, 20, 30])
# random_thought = {
#     (10, 20, 30),
#     'Patrik',
#      True,
#         1,
#         1, 
#         4
# }
# print(random_thought)

# print(random_thought)

# print(1 is True)

# import sys
# print(sys.getsizeof(8388608009888888888555555555555555555555555555555554444444444442222222222222222222222222222222222222222222222222222222222222222222222222222233333333333333333333333333333))
# print(sys.getsizeof(True))

# Dictionary
# syntax 
""" 
var = {
    # key(immutable type) : value(any valid type)
    "Name" : 'Suman', 
     20    : 30,
     [1, 2]: 'Something' # error
}
var = dict()
"""

# my_list = [1, 4, 5, 6]
# print(my_list[2])

# database = {
#     'Name': ['Suman', 'Patrik', 'Foo', 'Bar'],
#     'age':[100, 100, 20, 30]
# }

# database['Extra'] = 101

# rs = input() # Name
# print(rs)
# print(database[rs]) # database['Name']
# print(database)
# values = database.values()
# print(values, end='\n\n')
# print(type(values))
# print(database['Name'][0]) # will fetch 'Suman'

# print('All the  keys', '*' * 40)
# for key in database.keys():
#     print(key)

# print('All the  valuess', '*' * 40)
# for value in database.values():
#     print(value)

# print("*" * 50)

# for key, value in database.items():
#     print(key, value)


# database = {
#     'Name': ['Suman', 'Patrik', 'Foo', 'Bar'],
#     'age':[100, 100, 20, 30]
# }

# print(database)
# database['age'].append(999)
# # database['age'] = [400,]
# print(database)

# numbers = [1, 2, 3, 4]
# numbers[3] = 10 # [1, 2, 3, 10]

# numbers = [10, 20, 33, 44]
# for num in numbers:
#     print(num)

# for index, value in enumerate(numbers): index, (key, value)
#     #print(index, value)
#     # Index is : ___ and the value is ___
#     print(f'Index is : {index} and the value is : {value}')

# database = dict()
# database['Name'] = ['Suman', 'Patrik', 'Foo', 'Bar']

# database = {
#     'Name': ['Suman', 'Patrik', 'Foo', 'Bar'],
#     'age':[100, 100, 20, 30],
#      12 : '2012'
# }

# print(database['Name'][2])
# print(database['Name'])
# print(database[12])
# print(database.keys())
# print(database.values())
# print(database.items())

# # a, b = 10, 20
# # a, b = (10, 20)
# # (a, b) = (10, 20)

# for key, value in database.items():
#     print(key, value)


# for (key, value) in database.items():
#     print(key, value)

# for index, (key, value) in enumerate(database.items()): #index, (key, value)
#     # enumerate(0, ('Name', ['Suman', 'Patrik', 'Foo', 'Bar']))
#     print(index, key, value)

# (x, a), b = 8, (10, 20)
# print(x, a, b)
# x,(a,b) = 10, (20, 40) # this is good
# x, a, b = 10, (20, 40) # this will cause error
# a, b = (10, 20, 30) # this too will causse an error


# numbers = [1, 2, 4, 5]
# for index, number in enumerate(numbers, start=10):
#    print(f'Index is : {index} and the value is : {number}')


    
