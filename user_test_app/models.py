from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings



# Create your models here.
class TestUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class UserActivity(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_activity',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)