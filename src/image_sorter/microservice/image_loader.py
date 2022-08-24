from image_sorter.communication.rabbitmq import Singleton


class ImageLoader(metaclass=Singleton):
    def __init__(self, channel) -> None:
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    def send_picture(self):
        pass
