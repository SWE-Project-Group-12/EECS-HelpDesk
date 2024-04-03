from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from login.models import Student


class Feedback(models.Model):
    feature = models.TextField(null=False, blank=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(null=False, blank=False)
    dateCreated = models.DateField(auto_now_add=True)
    username = models.ForeignKey(to=Student, on_delete=models.CASCADE)