from django.db import models
from .ticket import Ticket


class TechnicalFault(Ticket):
    # Standard Model. Inherits from the Model Ticket.
    # Used to store Technical Faults.
    ITL = "ITL"
    ITS = "ITS"
    Library = "Library"
    NONE ="NONE"

    LOCATION_CHOICES = {
        ITL: "ITL",
        ITS: "ITS",
        Library: "Library",
        NONE: "None",
    }

    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
