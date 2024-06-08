from django.core.management.base import BaseCommand
from myapp.models import Conversation
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete conversations older than a specified number of days'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=30,
            help='Delete conversations older than this number of days (default: 30)'
        )

    def handle(self, *args, **options):
        days = options['days']
        threshold_date = timezone.now() - timedelta(days=days)
        old_conversations = Conversation.objects.filter(created__lt=threshold_date)
        count = old_conversations.count()
        old_conversations.delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} old conversations'))
