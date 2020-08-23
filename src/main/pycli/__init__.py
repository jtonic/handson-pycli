import click


@click.group()
def main():
    pass


@main.command("hello")
@click.option('--count', '-c', default=1, help='Number of greetings', type=int,
              required=True, show_default=True)
@click.option('--name', '-n', prompt='Your name', help='The person to greet', type=str,
              required=True, show_default=True)
def _hello(count: int, name: str):
    """It greets NAME for a total of COUNT times"""
    for _ in range(count):
        click.echo(f'Hello {name}')


@main.command("sum")
@click.option('-a', prompt='a', help='First operand', type=int,
              required=True)
@click.option('-b', prompt='b', help='2nd operand', type=int,
              required=True)
def _sum(a: int, b: int):
    """
    Sum a and b.

    :param a: first operand

    :param b: second operand

    :return: the sum
    """
    click.echo(a + b)
