
# Setup Project 101

## Virtual environment

1. Create virtual environment.
``` bash
        python -m venv name_of_the_env
```
        
2. Activate virual environment.

    - Windows
    
        ``` bash
        name_of_the_env\Scripts\activate
        ```
    - Linux
         ``` bash
        source name_of_the_env\Scripts\activate

3. Deactivate virual environment.
``` bash
    deactivate
```

## PIP 

1. Install library.
``` bash
    pip install lib_name
```

2. Check all the libraries.
``` bash
    pip list
```

3. Create requirements.txt 
``` bash
    pip freeze > requirements.txt 
```