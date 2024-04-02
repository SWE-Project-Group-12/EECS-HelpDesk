from django.db import models
from .ticket import Ticket


class TechnicalFault(Ticket):
    # Standard Model. Inherits from the Model Ticket.
    # Used to store Technical Faults.
    ITL = "ITL"
    ITS = "ITS"
    Library = "Library"
    QMplus = "QMplus"
    Mysis = "Mysis"
    Other = "Other"

    LOCATION_CHOICES = {
        ITL: "ITL",
        ITS: "ITS",
        Library: "Library",
        QMplus: "QMplus",
        Mysis: "Mysis",
        Other: "Other",
    }

    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
