import click
import click_completion
from pycli.template import render, walk_templates_dir


click_completion.init()


@click.group()
def main():
    pass


@main.command("hello")
@click.option(
    "--count",
    "-c",
    default=1,
    help="Number of greetings",
    type=int,
    required=True,
    show_default=True,
)
@click.option(
    "--name",
    "-n",
    prompt="Your name",
    help="The person to greet",
    type=str,
    required=True,
    show_default=True,
)
def _hello(count: int, name: str) -> None:
    """It greets NAME for a total of COUNT times"""
    for _ in range(count):
        click.secho(f"Good {name}", fg="green")
        click.secho(f"Bad {name}", fg="red", bold=True)


@main.command("sum")
@click.option("-a", prompt="a", help="First operand", type=int, required=True)
@click.option("-b", prompt="b", help="2nd operand", type=int, required=True)
def _sum(a: int, b: int) -> None:  # pylint: disable=C0103
    """
    Sum a and b.

    :param a: first operand

    :param b: second operand

    :return: the sum
    """
    click.echo(a + b)


@main.command("produce-message")
@click.option(
    "--templates-dir",
    default="templates",
    prompt="Templates directory",
    help="Templates dir",
    type=str,
    required=True,
    show_default=True,
)
@click.option(
    "--template-file",
    default="index.html.j2",
    prompt="Template file",
    help="Template file",
    type=str,
    required=True,
    show_default=True,
)
def produce_message(templates_dir: str, template_file: str) -> None:
    """Produce a message by rendering a template"""

    walk_templates_dir(templates_dir)
    content = render(templates_dir=templates_dir, template_file=template_file)
    click.echo(f"Rendered content: {content}")


if __name__ == "__main__":
    main()
