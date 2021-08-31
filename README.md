
# CTCJ 
## Virtual environment

1. Create virtual environment.
``` bash
    python -m venv name_of_the_env
```
        
2. Activate virual environment.

    - Windows 😪
    
        ``` bash
        name_of_the_env\Scripts\activate
        ```
    - Linux 😃
         ``` bash
        source name_of_the_env/bin/activate
        ```
3. Deactivate virual environment.
``` bash
    deactivate
```

## PIP 

1. Install library.
``` bash
    pip install lib_name
```

2. Uninstall library.
``` bash
    pip uninstall lib_name
```

3. Install all from requirments.txt
``` bash
    pip install -r requirments.txt
```

4. Check all the libraries and the version.
``` bash
    pip list
```

5. Create requirements.txt 
``` bash
    pip freeze > requirements.txt 
```


## Github -> Your computer

1. git clone.
``` bash
    git clone https://github.com/Patrik-cosmic/ctcj.git
```

## Variable / Identifier
``` python
var = some_value_of_some_valid_type

1: case sensitive ('name' is not 'Name' or 'NAME' or 'nAME' etc)

2: must_contains (a-z)(A-Z)(0-9)(_)
        a. must start with (a-z)(A_Z)(_)
        
        2name = ❌
        _name = 🆗
        name  = 🆗
        Name  = 🆗
        Name2 = 🆗


3: can't be keywords 

    ['False', 'None', 'True', 'and', 'as', 'assert', 
'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 
'yield']

     pass = ❌ 
     pass123 = 🆗


5:  lower_case, snake_case (date_of_birth)

 - Type 

     1: _var     ('Internal use or private)

     2: __var    ('class specific')

     3: __var__  ('system-defined')

```
