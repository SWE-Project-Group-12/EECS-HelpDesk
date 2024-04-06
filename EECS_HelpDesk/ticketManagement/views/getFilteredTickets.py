def getFilteredTickets(model, filters):
    temp = []
    for filter in filters:
        temp += model.objects.filter(**filter)
    return temp