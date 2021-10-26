from pycli.application_conf import load_conf, Application, parse

APP_DESCRIPTION = "PyCli Application"
APP_NAME = "PyCli"


def test_load_conf():
    app: Application = load_conf()
    assert app.name == APP_NAME
    assert app.description == APP_DESCRIPTION


def test_parse():
    app = parse(
        {"application": Application(name="PyCli", description="PyCli Application")}
    )

    assert app.name == "PyCli"
    assert app.description == APP_DESCRIPTION
