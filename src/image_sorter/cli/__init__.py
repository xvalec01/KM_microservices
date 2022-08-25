import click
import os
import sys
from image_sorter.microservice.image_sorter import ImageSorter
from image_sorter.microservice.image_processor import ImageProcessor
from image_sorter.microservice.image_loader import ImageLoader


@click.group()
def cli():
    pass


@cli.command()
def start():
    print("Image sorter")
