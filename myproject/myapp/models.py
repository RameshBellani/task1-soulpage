from django.db import models
from django.utils import timezone
from nltk.tokenize import sent_tokenize


class Conversation(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.summary:
            self.summary = self.generate_summary()
        super().save(*args, **kwargs)

    def generate_summary(self):
        sentences = sent_tokenize(self.content)
        summary = ' '.join(sentences[:2])
        return summary

    def __str__(self):
        return self.title
