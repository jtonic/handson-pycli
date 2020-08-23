from pycli.application_conf import load_conf, Application, parse


def test_load_conf():
    app: Application = load_conf()
    assert app.name == 'PyCli'
    assert app.description == 'PyCli Application'


def test_parse():
    app = parse({"application": Application(name='PyCli', description='PyCli Application')})

    assert app.name == 'PyCli'
    assert app.description == 'PyCli Application'
