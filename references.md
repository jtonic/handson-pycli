# Useful things

## pyenv useful commands
---

- `pyenv commands` - list commands

- `pyenv install --list` - list available python versions (and more)

- `pyenv install -v 3.8.2` - install a python version

- `pyenv uninstall 3.8.2` - uninstall a python version

- Remove all pyenvs `rm -rf ~/.pyenv/versions` - remove all python version installed with pyenv

- `pyenv versions` - show installed python versions

- `pyenv version` - show current python version

- `pyenv which python`

- `pyenv which pip`

- `pyenv local 3.8.2` set the current python for the project

- `pyenv shell 3.9-dev` runa

- `pyenv virtualenv 3.8.2 pycli-python3.8.2` create a virtualenv

- `pyenv virtualenvs` show all virtual environments

## How to create the source and wheel distributions

- `python -m pip install --upgrade pip setuptools wheel` upgrade pip, setuptools and wheel

- `python setup.py sdist bdist_wheel` create the distributions

## Python useful commands

- run pip with python `python -m pip --version`

- test the installation with builtin tests `python -m test`

## Documentation references

- [pyenv issue when installed with brew](https://stackoverflow.com/a/34156303/1102761)
- [setuptools - entry_points](https://stackoverflow.com/a/9615473/1102761)
- [pyenv intro](https://realpython.com/intro-to-pyenv/)
- [visual pytest-ing in Idea/Pycharm](https://blog.jetbrains.com/pycharm/2020/06/visual-testing-with-pytest/)
- [String formatting](https://realpython.com/python-string-formatting/)
- [String dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [tox](https://opensource.com/article/19/5/python-tox)
- [pycharm/idea tox - 1](https://www.jetbrains.com/help/pycharm/tox-support.html)
- [pycharm/idea tox - 2](https://www.jetbrains.com/help/pycharm/run-debug-configuration-tox.html)
- [pytest - 1](https://docs.pytest.org/en/latest/getting-started.html)
- [pytest - 2](https://dzone.com/articles/10-awesome-features-of-pytest)
- [pytest - 3](https://towardsdatascience.com/pytest-features-that-you-need-in-your-testing-life-31488dc7d9eb)
- [pytest gherkin](https://pypi.org/project/pytest-bdd/#:~:text=pytest-bdd%20implements%20a%20subset,power%20and%20flexibility%20of%20pytest.)
- [pytest-bdd](https://github.com/pytest-dev/pytest-bdd)
- [pytest-bdd in pycharm/idea](https://blog.jetbrains.com/pycharm/2018/08/pycharm-and-pytest-bdd/)
- [python cli with click](https://click.palletsprojects.com/en/7.x/)
- [Jinja2 templates](https://jinja.palletsprojects.com/en/2.11.x/templates/)
- [Jinja2 API](https://jinja.palletsprojects.com/en/2.11.x/api/#basics)
