import logging


class Dispatcher:
    def __init__(self, channel):
        self._channel = channel

    def send(self, payload, context):
        logging.info("Sending: %r" % (payload))
        self._channel.basic_publish(
            exchange=context.exchange,
            routing_key=context.routing_key,
            body=payload,
        )

    def receive(self, context):
        def callback(ch, method, properties, body):
            print("Received %r" % body)

        self._channel.basic_consume(
            queue=context.queue, on_message_callback=callback, auto_ack=True
        )
        self._channel.start_consuming()
