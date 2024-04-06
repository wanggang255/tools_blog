from django.db import models
from mdeditor.fields import MDTextField
from django.utils.timezone import now
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField('title', max_length=200, unique=True)
    content = MDTextField("content")
    create_time = models.DateTimeField("create_time", blank=False, null=False, default=now)
    last_update_time = models.DateTimeField("last_update_time", blank=False, null=False, default=now)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='author',
        blank=False,
        null=False,
        on_delete=models.CASCADE)
