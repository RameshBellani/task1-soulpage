from django.test import TestCase

# Create your tests here.
from celery import shared_task
from .models import Conversation
from datetime import timedelta
from django.utils import timezone

@shared_task
def cleanup_old_conversations(days=30):
    threshold_date = timezone.now() - timedelta(days=days)
    old_conversations = Conversation.objects.filter(created__lt=threshold_date)
    old_conversations.delete()
