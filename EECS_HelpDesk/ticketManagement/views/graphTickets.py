from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .getUserType import getUserType
from datetime import datetime, timedelta
import json


class GraphTickets(ListView):
    template_name = "graphTickets.html"
    model = None
    authorised_users = []
    ticket_type = None
    ticket_type_display = None

    def get(self, request, *args, **kwargs):
        if request.session.get("user") is None:
            return HttpResponseRedirect("/login")

        username = request.session.get("user")
        if getUserType(username) not in self.authorised_users:
            return HttpResponseRedirect("/listAll" + self.ticket_type.replace(" ", "") + "s")

        totalEachDayForLast7Days = {}
        totalLast7days = 0
        totalLast30days = 0

        for x in range(1, 8):
            dateToGet = (datetime.now() - timedelta(days=x))
            formattedDate = dateToGet.strftime("%Y-%m-%d")
            totalLast7days += len(self.model.objects.filter(dateCreated=formattedDate).values())
            totalEachDayForLast7Days[dateToGet.strftime("%b %d, %Y")] = len(self.model.objects.filter(dateCreated=formattedDate).values())


        for x in range(1, 31):
            dateToGet = (datetime.now() - timedelta(days=x)).strftime("%Y-%m-%d")
            totalLast30days += len(self.model.objects.filter(dateCreated=dateToGet).values())

        data = {
            "totalEachDayForLast7Days": list(totalEachDayForLast7Days.values())[::-1],
            "eachDayForlasy7Days": list(totalEachDayForLast7Days.keys())[::-1],
            "totalLast7days": totalLast7days,
            "totalLast30days": totalLast30days,
        }

        return render(request, self.template_name, {"data": json.dumps(data), "username": username, "userType": getUserType(username), "ticketType": self.ticket_type_display})