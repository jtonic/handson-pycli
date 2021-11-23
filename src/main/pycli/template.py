import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pycli.definitions import ROOT_DIR


def render(templates_dir, template_file):
    templates_dir = os.path.join(ROOT_DIR, templates_dir)
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


def walk_templates_dir(templates_dir: str) -> None:
    dest_dir = "/Users/antonelpazargic/jtonic/git/github/handson-pycli/destination"
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    else:
        exit(1)

    for root, _, files in os.walk(templates_dir):
        path = root.split(os.sep)
        print((len(path) - 1) * "--", os.path.basename(root))
        # path diffs between templates_dir and root
        new_dir = os.path.join(dest_dir, os.path.basename(root))
        os.makedirs(new_dir)
        for file in files:
            print(len(path) * "--", file)
