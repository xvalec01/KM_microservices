import os

from image_sorter.communication.dispatcher import Dispatcher
from image_sorter.communication.rabbitmq import (
    ContextConfiguration,
    RabbitMQ,
    Singleton,
)
from image_sorter.core.constants import IMAGE_DIR


class ImageLoader(metaclass=Singleton):
    def __init__(self, context: ContextConfiguration) -> None:
        self.context = context
        self._rabbitmq = RabbitMQ(context=self.context)
        self.name = "ms-loader"

    def load_pictures(self):
        for filename in os.scandir(IMAGE_DIR):
            if filename.is_file():
                print(filename.path)

    def send_picture(self):
        dispatcher = Dispatcher(self._rabbitmq.channel)
        dispatcher.receive(self.context)
        self._rabbitmq.connection.close()
