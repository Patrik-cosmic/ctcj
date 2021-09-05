# eval function

# my_string = input('Give me an expression: ')
# result = eval(my_string)
# print(result)

# def function_name(parameter(optional)):
    # ...
    # return value (optional)

# def even_odd_check(number): # signature of the function
#     if number%2 == 0:
#         # The number 2 is even
#         print(f'The number {number} is even')
#     else:
#         # The number 3 is odd
#         print(f'The number {number} is odd')


# # function call 
# # function_name(argunments)

# num = 25
# even_odd_check(num) 

# def thakur_ghar():
#     prosad = 'Batasa and Nokuldana'
#     extra = 'Pipre, tulsi pata, bel pata'
#     return prosad, extra
#     #return 'valo_prosad' + ' kichu pipre'
    

# prosad, extra = thakur_ghar() # (prosad, extra)

# print(prosad)
# print(extra)

#print('valo_prosad' + 'kichu pipre')

# def add(number1, number2):
#     return number1 + number2

# print(add(5, 15))

# def add(number1, number2 = 25):
#     return number1 + number2

# print(add(5))

# def add(number1, number2 = 25):
#     return number1 + number2

# print(add(5, 15))

# def add_gen(*numbers): 
    # print(numbers)
    # print(type(numbers))
    # print(sum(numbers))

    # return sum(numbers) # way 1

    # sum = 0   # Way 2
    # for num in numbers:
    #     sum = sum + num
    # return sum

#     sum = 0 # Way 3
#     for num in numbers:
#         if num%2 == 0:
#              sum = sum + num
#     return sum

# print(add_gen(1, 2, 3, 4, 5, 6, 7, 8))
# print(add_gen(1, 2, 3, 4, 5))
# print(add_gen(1, 2, 3, 4))
# print(add_gen(1, 2))      # will return  3
# print(add_gen(1))         # will return  1
# print(add_gen())          # will return  0 

# def arijit():
#     print('Hello dada bolchilam amar ekta prosno achay')

# def ajim():
#     print('Dada ami chilam na sunte paini')


# student = ['arijit', 'ajim']

# for person in student:
#     eval(person+'()') # func_name() => 'arijit()' => 'ajim()'