import nltk
from nltk.tokenize import sent_tokenize
from django.db import models

nltk.download('punkt')

class Conversation(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.summary:
            self.summary = self.generate_summary()
        super().save(*args, **kwargs)

    def generate_summary(self):
        sentences = sent_tokenize(self.content)
        summary = ' '.join(sentences[:2])  # Simple summary: first 2 sentences
        return summary

    def __str__(self):
        return self.title
