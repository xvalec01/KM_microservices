from image_sorter.communication.rabbitmq import (
    Singleton,
    RabbitMQ,
    ContextConfiguration,
)


class ImageProcessor(metaclass=Singleton):
    def __init__(self, context: ContextConfiguration) -> None:
        self._rabbitmq = RabbitMQ(context=context)
        self.name = "ms-processor"
