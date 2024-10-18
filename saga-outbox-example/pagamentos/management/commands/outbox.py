import time

from django.core.management.base import BaseCommand
from django.utils import timezone

from ...app.pubsub import process_outbox


class Command(BaseCommand):
    help = "Process outbox messages"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting outbox processor"))

        while True:
            start_time = timezone.now()

            process_outbox()

            end_time = timezone.now()
            processing_time = (end_time - start_time).total_seconds()

            sleep_time = max(10 - processing_time, 0)
            time.sleep(sleep_time)

        self.stdout.write(self.style.SUCCESS("Outbox processor finished"))
