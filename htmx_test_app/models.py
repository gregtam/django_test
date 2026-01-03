from django.db import models
from django.conf import settings

# Create your models here.
class Counter(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='counter',
        null=True,
        blank=True
    )

    count = models.IntegerField(default=0)