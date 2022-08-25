import os

from image_sorter.communication.dispatcher import Dispatcher
from image_sorter.communication.rabbitmq import (
    ContextConfiguration,
    RabbitMQ,
    Singleton,
)
from image_sorter.core.constants import IMAGE_DIR


class ImageLoader(metaclass=Singleton):
    """
    Microservice solving loading images.
    :param context: The context is used to store metadata about rabbitmq connection
    :type context: ContextConfiguration
    :ivar context: storing Context
    :vartype context: ContextConfiguration
    :ivar _rabbitmq: RabbitMQ class initiating RabbitMQ connection
    :vartype _rabbitmq: RabbitMQ
    """

    def __init__(self, context: ContextConfiguration) -> None:
        self.context = context
        self._rabbitmq = RabbitMQ(context=self.context)
        self.name = "ms-loader"

    def load_pictures(self):
        dispatcher = Dispatcher(self._rabbitmq.channel)
        for filename in os.scandir(IMAGE_DIR):
            with open(filename), "rb" as f:
                data = f.read()
                dispatcher.send(payload=data)

    def send_picture(self):
        dispatcher = Dispatcher(self._rabbitmq.channel)
        dispatcher.receive(self.context)
        self._rabbitmq.connection.close()
