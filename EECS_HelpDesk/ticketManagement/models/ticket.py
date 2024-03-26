from django.db import models

UPDATED = "UPDATED"
VOID = "VOIDED"
PENDING = "PENDING"

STATUS_CHOICES = {
		UPDATED: "Updated",
		VOID: "Void",
        PENDING: "Pending",
	}
class Ticket(models.Model):
    # Abstract Model (See https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance).
    # Contains the common attributes for ECs and Technical Faults.

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    dateCreated = models.DateField(auto_now_add=True)
    status_update_reason = models.CharField(max_length=150, default="")
    username = models.ForeignKey(to="login.Student", on_delete=models.CASCADE)


    class Meta:
        abstract = True