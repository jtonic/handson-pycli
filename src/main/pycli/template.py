from os import path

from jinja2 import Environment, FileSystemLoader
from pycli.definitions import ROOT_DIR


def render():
    templates_dir = path.join(ROOT_DIR, 'templates')
    file_loader = FileSystemLoader(templates_dir)
    env = Environment(loader=file_loader)
    template = env.get_template('index.html')
    html = template.render({'title': 'Tool', 'header': 'Menu', 'body': 'CD Pipeline'})
    return html
