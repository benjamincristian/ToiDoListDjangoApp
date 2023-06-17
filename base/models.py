from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
