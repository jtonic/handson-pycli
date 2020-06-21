from pycli.application_conf import load_conf, Application


def test_load_conf():

    app: Application = load_conf()
    assert app.name == 'PyCli'
    assert app.description == 'PyCli Application'
