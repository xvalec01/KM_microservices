from image_sorter.communication.rabbitmq import (
    ContextConfiguration,
    RabbitMQ,
    Singleton,
)


class ImageSorter(metaclass=Singleton):
    def __init__(self, context: ContextConfiguration) -> None:
        self._rabbitmq = RabbitMQ(context=context)
        self.name = "ms-sorter"
