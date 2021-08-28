print("Hello");
print('Hello') # this one is good 

# Variable / Identifier

# var = some_value_of_some_valid_type
""" props
1: case sensitive ('name' is not 'Name' or 'NAME' or 'nAME' etc)

2: must_contains (a-z)(A-Z)(0-9)(_)
        - must start with (a-z)(A_Z)(_)
        2name = ❌ 
        _name = 🆗
        name  = 🆗
        Name  = 🆗
        Name2 = 🆗


3: can not be keywords 

    ['False', 'None', 'True', 'and', 'as', 'assert', 
'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 
'yield']

     pass = 12 ❌ 
     pass123 = 🆗

4:   1: _var     ('Internal use or private)

     2: __var    ('class specific')

     3: __var__  ('system-defined')


5:  lower_case, date_of_birth (snake_case)

"""

name = 'Suman De'
print(type(name))
print(type('Suman De'))

number1 = 123
print(type(number1))
print(type(123))

number2 = 123.36
print(type(number2))
print(type(123.36))

condition = True
print(type(condition))
print(type(True))

""" invalid type
random = *9464563*****
print(type(random))
print(type(*9464563*****))
"""
# valid again :)
random = '*9464563*****'
print(type(random))
print(type('*9464563*****'))