from django.db import models


class Ticket(models.Model):
    # Abstract Model (See https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance).
    # Contains the common attributes for ECs and Technical Faults.

    UPDATED = "UPDATED"
    VOID = "VOIDED"

    STATUS_CHOICES = {
		UPDATED: "Updated",
		VOID: "Void",
	}


    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    # add username field 


    class Meta:
        abstract = True