import logging

import pika


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ContextConfiguration:
    def __init__(
        self,
        routing_key=None,
        receiver=False,
        host="localhost",
        queue=None,
        exchange=None,
    ):
        self.host = host
        self.queue = queue
        self.routing_key = routing_key
        self.exchange = exchange
        self.receiver = receiver


class RabbitMQ(metaclass=Singleton):
    def __init__(self, context: ContextConfiguration):
        self.context = context
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.context.host)
        )

        self._channel = self._connection.channel()
        self._channel.exchange_declare(
            exchange=self.context.exchange_name, exchange_type="direct"
        )
        if self.routing_key is not None:
            self._channel.queue_bind(
                exchange=context.exchange_name,
                queue=context.queue,
                routing_key=context.routing_key,
            )
        if self.context.queue is None:
            self.context.queue = ""
            result = self._channel.queue_declare(queue=self.context.queue, durable=True)
            self.context.queue = result.method.queue

    @property
    def channel(self):
        return self._channel

    @property
    def connection(self):
        return self._connection

    def __del__(self):
        """
        Only if the connection is made by receiver create queue for direct communication
        """
        self._connection.close()
