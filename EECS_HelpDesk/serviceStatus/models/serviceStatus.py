from django.db import models

SERVICE_STATUS_CHOICES = {
		"Good Service": "Good Service",
		"Partial Service": "Partial Service",
        "No Service": "No Service",
	}


class serviceStatus(models.Model):

    service_name = models.CharField(max_length = 35, primary_key = True)
    status = models.CharField(max_length = 20, choices=SERVICE_STATUS_CHOICES, default=SERVICE_STATUS_CHOICES['Good Service'])
    status_description = models.CharField(max_length = 128, default="", null = True, blank= True) 