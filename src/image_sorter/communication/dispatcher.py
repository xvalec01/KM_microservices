from multiprocessing import context
import os
import sys
import logging


class Dispatcher:
    def __init__(self, channel):
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    def send(self, payload, context):
        logging.info("Sending: %r" % (payload))
        self._channel.basic_publish(
            exchange=context.exchange,
            routing_key=context.routing_key,
            body=payload,
        )

    def receive(self, context):
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        self.channel.basic_consume(
            queue=context.queue, on_message_callback=callback, auto_ack=True
        )
        self.channel.start_consuming()


disp = Dispatcher()
disp.send()
try:
    disp.receive()
except KeyboardInterrupt:
    print("Interrupted")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
