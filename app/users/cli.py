import click
from plain.cli import register_cli


@register_cli("users")
@click.group()
def cli():
    """Custom app.users commands"""
    pass


@cli.command()
@click.option("--email", prompt="Email", help="The email address of the user")
@click.option(
    "--password", prompt="Password", help="The password of the user", hide_input=True
)
def create_admin(email, password):
    """Create an admin user"""
    from .models import User

    User.objects.create(email=email, password=password, is_admin=True)
    click.secho(f"{email} created as an admin", fg="green")
