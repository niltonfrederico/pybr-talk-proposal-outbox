from uuid import uuid4

from django_stomp.services.consumer import Payload
from django_stomp.services.producer import auto_open_close_connection
from django_stomp.services.producer import build_publisher
from django_stomp.services.producer import do_inside_transaction


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


def consumer(payload: Payload):
    payload_body, payload_headers = payload.body, payload.headers
    print(
        f"Received payload with body: {payload_body} and headers: {payload_headers} for callback actions consumer.",
    )

    try:
        raise Exception("Erro externo!")
    except Exception as e:
        print(f"Erro: {e}")

        return payload.ack()
