import os
import sys

import click

from image_sorter.communication.rabbitmq import ContextConfiguration
from image_sorter.microservice.image_loader import ImageLoader
from image_sorter.microservice.image_processor import ImageProcessor
from image_sorter.microservice.image_sorter import ImageSorter


@click.group()
def cli():
    pass


@cli.command()
def start():
    context = ContextConfiguration(routing_key="images", exchange="image-loader")
    ms_image_loader = ImageLoader(context=context)
    ms_image_loader.send_picture()
