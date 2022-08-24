import click
import os
import sys


@click.group()
def cli():
    pass


@cli.command()
def start():
    print("Image sorter")
