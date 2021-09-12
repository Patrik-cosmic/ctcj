# revise again and again 
# def add(*numbers): # *args
#     print(type(numbers))
#     return sum(numbers)

    # sum = 0
    # for num in numbers:
    #     sum = sum + num
    # return sum

# print(add())
# print(add(2))
# print(add(2,5))
# print(add(2,3,5))

# all_numbers = [1, 4, 5, 6, 7]
# print(all_numbers, sep='\t')
# print(*all_numbers, sep='\t')

# print(add(*all_numbers))

# print(sum(all_numbers, 3))



# def info_student(name, roll, section):
#     print(name, roll, section, sep=' -> ')

# def info_employee(name, id, dept, tech, salary, exp):
#    pass
#    # or
#    ...

# info_student('Suman De', 2, 'M.Sc.')

# def info(**attrs): #**kwargs
#     print(type(attrs), end='\n\n')
#     print(attrs, end='\n\n')
#     print(attrs.keys(), end='\n\n')
#     print(attrs.values(), end='\n\n')
#     print(attrs.items(), end='\n\n')

#     # emp specific condition 
#     if 'tech' in attrs:
#         print(attrs['tech'])
#     else:
#         print("The key tech is not present \n")

# info_suman = {
#     "name": 'Suman',
#     "id": 2,
#     "dept": 'M.Sc.'
# }
# info(**info_suman)

# print(info_suman)

# print(**info_suman) # error

# Solution 
# def test(id, dept, name):
#     print(name)
#     print(id)
#     print(dept)
# test(**info_suman)
# print(*info_suman)


# def greet(message, name):
#     print(f'{message} {name}')


# greet(name='Suman',message='Good morning')




# info(name='Suman De', id = 2, dept = 'M.Sc.')
# info(name='Patrik Dark', id=102, dept='Full stack', tech=['Python','Django','React','PGSQL'], salary=9999999, exp=6)

# def func_name(*args, **kwargs):
#     print(args)
#     print(sum(args))
#     print(args.index(3))

#     print(kwargs)
#     print(kwargs.keys())
#     for key, value in kwargs.items():
#         print(f'Key is: {key} and the value is: {value}')

# func_name(1, 2, 3, 4, 5, name = 'Suman De', computer = 'Laptop')
# func_name(1, 2, 3, 4, 5, name = 'Suman De', computer = 'Laptop', 9) # home task about this error



# numbers = [1,]
# print(type(numbers))
