# A simple python cli project

## Steps

- [x] create pyenv/virtual env (python v.3.8.2)
- [x] setup.py
- [x] src/pycli
- [x] tests
- [x] setup in IntelliJ Idea
- [x] create a simple main (bootstrap)
- [x] create a simple test
- [ ] @dataclass
- [ ] simple cli command with click
- [ ] configure the pylint
- [ ] create a python script
- [ ] publish the python script on pypi
- [ ] create github actions to build the application run the tests

## Howto

- Create the python script command

```shell script
  $ python -m pip install -e .
  # restart shell
  $ pycli 
```

- install the extra tests pytest dependency

    `pip install -e '.[tests]'` (for sh), or 
    
    `pip install -e .[tests]` (shell)

- run tests `pytest` 


Caveats:

- If python cannot be installed because curl doesn't support https protocol try this

```shell script
    $ brew remove curl
    $ brew remove curl-openssl
    $ echo 'export PATH="/usr/local/opt/curl-openssl/bin:$PATH"' >> ~/.zshrc
    $ source ~/.zshrc
    # or 
    $ echo 'export PATH="/usr/local/opt/curl-openssl/bin:$PATH"' >> ~/.bash_profile  
    $ source ~/.bash_profile
```

- If somehow, after the pyenv virtualenv python installation the virtual env is not shown into terminal (after shell restart) then:

    - check to see if you have the following lines in ~/.bash_profile or ~/.zshrc
    
```shell script
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
