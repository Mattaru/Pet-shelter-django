import uuid

from django.urls import reverse

from django.db import models

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    author_name = models.CharField(verbose_name='Author name', max_length=50)
    title = models.CharField(verbose_name='Title', max_length=300)
    message_data = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'{self.author_name} ({self.title})'
