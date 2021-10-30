# A simple python cli project

## Steps

- [x] create pyenv/virtual env (python v.3.8.2)
- [x] setup.py
- [x] src/pycli
- [x] tests
- [x] setup in IntelliJ Idea
- [x] setup in vs code (I love its python development experience)
- [x] create a simple main (bootstrap)
- [x] create a simple test
- [x] Simple @dataclass
- [x] Create the source and wheel binary distributions
- [x] Load and parse a yaml file to a custom python type (class)
- [x] Include data files from packages in the source and binary distributions
- [x] simple cli command with click
- [x] simple cli to render a Jinja2 template
- [ ] Include data files from file system in the source and binary distributions
- [ ] run test with different pyenv/virtualenv configurations with tox
- [x] configure the pylint
- [ ] pytest-bdd gherkin example (test the support in idea)
- [x] create a python script for simple py-cli
- [ ] publish the python script on pypi
- [x] create github actions to build the application run the tests


## Howto

- install the dev dependencies

```shell script
    pip install -e '.[dev]' # sh
    # OR
    pip install -e .[dev] # shell
    # OR even better
    pip install -r requirements.txt
```

- Create the python script command

  - version 1
  ```shell script
    # build the executable pycli
    $ python -m pip install -e .

    # restart shell
    $ pycli
  ```
  - version 2
  ```shell script
    # Run a cli command
    $ python src/main/pycli/main.py hello --count=2
  ```

- run tests

```shell script
    pytest
    # OR
    pytest -s # to always show in the console the print calls
    # OR
    python -m pytest
    # OR
    pytest --html=tests_report.html
```

- run pycli command

```shell script
    pycli --help
    # or
    pycli --count=3 --name=Tony
    # or
    pycli -c 3 -n Tony
    # or interactively
    pycli -c 3
    pycli
```

- enable shell completion

  - Run the following in the terminal
```shell script
eval "$(_PYCLI_COMPLETE=source pycli)"
```
  - or add it in .bashrc file

  Note: Further about this at:

  - [here](https://click.palletsprojects.com/en/6.x/bashcomplete/#activation)
  - [here](https://stackoverflow.com/a/52286575/1102761)


- run pylint

```shell script
  pylint src/main/pycli/ --output-format=text
  # or run it with html report
  pylint src/main/pycli/ | pylint-json2html -o pylint.html
```

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
export PATH="$(pyenv root)/shims:$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"
```

## References

- [here](./references.md)
