from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    object = models.Manager()