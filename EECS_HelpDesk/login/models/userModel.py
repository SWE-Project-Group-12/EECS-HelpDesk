from django.db import models

class User(models.Model):
    # Abstract Model (see https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance)
    # Contains common attributes for each type of user.
    name = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 25)
    username = models.CharField(max_length = 10, primary_key = True)
    password = models.CharField(max_length = 128) 

    class Meta:
        abstract = True
