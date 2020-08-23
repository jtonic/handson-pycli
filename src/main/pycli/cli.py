import click


@click.command()
@click.option('--count', '-c', default=1, help='Number of greetings', type=int,
              required=True, show_default=True)
@click.option('--name', '-n', prompt='Your name', help='The person to greet', type=str,
              required=True, show_default=True)
def hello(count: int, name: str):
    """It greets NAME for a total of COUNT times"""
    for _ in range(count):
        click.echo(f'Hello {name}')
