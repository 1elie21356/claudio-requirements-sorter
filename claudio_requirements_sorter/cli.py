import click

from claudio_requirements_sorter.sort_requirements import sort_requirements


@click.command()
@click.argument("source", type=click.File("r"))
@click.argument("destination", type=click.File("w"))
def main(source: click.File, destination: click.File) -> int:
    requirements = source.read().split()
    new_requirements = sort_requirements(requirements=requirements)
    destination.write("\n".join(new_requirements))

    click.echo(f"Successfully wrote to {destination.name}")
    return 0
