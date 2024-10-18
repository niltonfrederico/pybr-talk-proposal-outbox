from uuid import uuid4

from django_stomp.services.producer import auto_open_close_connection
from django_stomp.services.producer import build_publisher
from django_stomp.services.producer import do_inside_transaction

from .models import Outbox


def publish_to_queue(
    body: dict,
    queue: str,
    publisher_name: str | None = None,
    headers: dict | None = None,
):
    publisher = build_publisher(f"eiffel-tower{publisher_name}-{str(uuid4())}")
    with auto_open_close_connection(publisher), do_inside_transaction(publisher):
        if not headers:
            headers = {"correlation-id": uuid4().hex}

        publisher.send(
            body=body,
            headers=headers,
            queue=queue,
        )


def process_outbox():
    unpublished_messages = Outbox.objects.filter(published_at__isnull=True)
    for message in unpublished_messages:
        try:
            publish_to_queue(message, "/topic/estoque")
        except Exception as e:
            print(f"Failed to publish message {message.id}: {str(e)}")
