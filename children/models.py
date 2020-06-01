from django.db import models
from django.contrib.auth.models import User


class BlockedUrl(models.Model):
    url = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def validate_unique(self, exclude=None):
        qs = BlockedUrl.objects.filter(user=self.user)
        if qs.filter(url=self.url).exists():
            return False
        return True

    def save(self, *args, **kwargs):
        if self.validate_unique():
            super(BlockedUrl, self).save(*args, **kwargs)

