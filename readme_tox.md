# How to professionally work with python. Welcome tox.

## How to use pyenv, virtualenv and tox 

### Steps:

- Prerequisites:

    - Install the python versions used in tox.ini 
    
    ```shell script
    pyenv install 3.6.0
    pyenv install 3.7.0
    pyenv install 3.8.0
    ```

    - Install the virtualenvs for these 2 python versions
    
    ```shell script
    pyenv virtualenv 3.6.0 tox_3.6.0
    pyenv virtualenv 3.7.0 tox_3.7.0
    pyenv virtualenv 3.8.0 tox_3.8.0
    ```

    - Install tox and tox-pyenv in each of the virtual envs

    ```shell script
    pyenv activate tox_3.6.0 && pip install --upgrade pip && pip install tox tox-pyenv
    pyenv activate tox_3.7.0 && pip install --upgrade pip && pip install tox tox-pyenv 
    pyenv activate tox_3.8.0 && pip install --upgrade pip && pip install tox tox-pyenv 
    pyenv deactivate
    ```    

- Activate both virtualenvs locally (for the current project)
    
```shell script
pyenv local tox_3.6.0 tox_3.7.0 tox_3.8.0
```

- create `tox.ini` file in project root folder with the following content
    
```text
[tox]
envlist = tox_3.6.0,tox_3.7.0,tox_3.8.0
[testenv]
deps =
    pytest
    click
    pyyaml
commands = pytest
```

- run tox commands

```shell script
tox 
```

- configuration in IntelliJ Idea

    - setup the default testrunner
    - choose the correct python interpreter (sdk)
    - run tox commands 

## Documentation, references

-  
