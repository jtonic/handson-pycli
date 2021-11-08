from os import path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pycli.definitions import ROOT_DIR


def render(templates_dir, template_file):
    templates_dir = path.join(ROOT_DIR, templates_dir)
    file_loader = FileSystemLoader(templates_dir)
    env = Environment(
        loader=file_loader,
        autoescape=select_autoescape(
            enabled_extensions=("html", "xml", "json"), default_for_string=True
        ),
    )
    template = env.get_template(template_file)
    html = template.render({"title": "Tool", "header": "Menu", "body": "CD Pipeline"})

    return html
