import os

import click
from click import Path

from claudio_requirements_sorter.sort_requirements import sort_requirements


@click.command()
@click.argument("src", type=click.File("r"))
@click.argument("dst", type=click.File("w"))
def main(src: str, dst: str) -> int:
    requirements = src.read().split()
    new_requirements = sort_requirements(requirements=requirements)
    dst.write("\n".join(new_requirements))

    click.echo(f"Successfully wrote to {dst.name}")
    return 0
