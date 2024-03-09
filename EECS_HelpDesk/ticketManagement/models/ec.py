from django.db import models
from .ticket import Ticket


class EC(Ticket):
    # Standard Model. Inherits from the Model Ticket.
    # Used to store ECs.
    module = models.CharField(max_length=100)
    component = models.CharField(max_length=100)
