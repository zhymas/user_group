from django.db import models
from group.models import Group


class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, related_name='users')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return '/'

    def __str__(self):
        return self.username
