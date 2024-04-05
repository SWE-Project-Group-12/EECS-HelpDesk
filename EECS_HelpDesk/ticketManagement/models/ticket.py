from django.db import models


STATUS_CHOICES = {
		"Resolved": "Resolved",
		"Rejected": "Rejected",
        "Pending": "Pending",
	}

PRIORITY_CHOICES = {
    "Normal": "Normal",
    "High": "High",
    "Urgent": "Urgent",
}

class Ticket(models.Model):
    # Abstract Model (See https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance).
    # Contains the common attributes for ECs and Technical Faults.

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES['Pending'])
    dateCreated = models.DateField(auto_now_add=True)
    status_update_reason = models.CharField(max_length=150, default="")
    username = models.ForeignKey(to="login.Student", on_delete=models.CASCADE)
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES['Normal'])
    evidence = models.FileField(upload_to="evidence/", null=True, blank=True, default="")

    class Meta:
        abstract = True