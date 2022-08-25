from image_sorter.communication.rabbitmq import (
    Singleton,
    RabbitMQ,
    ContextConfiguration,
)


class ImageLoader(metaclass=Singleton):
    def __init__(self, context: ContextConfiguration) -> None:
        self._rabbitmq = RabbitMQ(context=context)
        self.name = "ms-loader"

    def send_picture(self):
        pass
