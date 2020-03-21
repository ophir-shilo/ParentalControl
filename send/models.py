from django.db import models
from django.contrib.auth.models import User


class KeyLog(models.Model):
    content = models.CharField(max_length=1000)
    writeTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class ScreenRecord(models.Model):
    record = models.FileField(default='output.avi', upload_to='records')
    writeTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class HistoryFile(models.Model):
    history = models.FileField(default='history', upload_to='histories')
    writeTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
