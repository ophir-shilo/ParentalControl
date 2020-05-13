from django.db import models
from django.contrib.auth.models import User


class BlockedUrl(models.Model):
    url = models.CharField(max_length=1000, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
