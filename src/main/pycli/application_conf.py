from dataclasses import dataclass
from os import path

import yaml
from pycli.definitions import ROOT_DIR

CONFIG_PATH = path.join(ROOT_DIR, "application.yaml")


@dataclass
class Application(yaml.YAMLObject):
    """
    Application configuration data class
    """

    yaml_tag = "!application"

    name: str
    description: str


def parse(conf: dict) -> Application:
    app_conf = conf["application"]
    return Application(app_conf.name, app_conf.description)


def load_conf() -> Application:
    with open(CONFIG_PATH) as file:
        yaml.add_path_resolver(tag="!application", path=["application"], kind=dict)
        conf = yaml.load(file, Loader=yaml.FullLoader)
        print(f"Configuration: {conf}")
        cfg: Application = parse(conf)
        print(f"Application: {cfg}")
        return cfg
