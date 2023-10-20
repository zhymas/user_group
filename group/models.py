from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return '/group/'

    def __str__(self):
        return self.name
