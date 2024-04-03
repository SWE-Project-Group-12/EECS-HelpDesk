from django.db import models


class FAQ(models.Model):
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)