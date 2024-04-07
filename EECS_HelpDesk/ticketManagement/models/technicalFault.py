from django.db import models
from .ticket import Ticket

ITL = "ITL"
ITS = "ITS"
Library = "Library"
QMplus = "QMplus"
Mysis = "Mysis"
Other = "Other"

LOCATION_CHOICES = {
    "ITL": "ITL",
    'ITS': "ITS",
    'Library': "Library",
    'QMplus': "QMplus",
    'Mysis': "Mysis",
    'Other': "Other",
}

class TechnicalFault(Ticket):
    # Standard Model. Inherits from the Model Ticket.
    # Used to store Technical Faults.

    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
