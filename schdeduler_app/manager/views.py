

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from manager.models import Event


class MainPage(View):
    def get(self, request):
        context = {}
        events = Event.objects.all()
        context['events'] = events
        return render(request, 'index.html', context)


class EventPage(View):
    def get(self, request):
        user = request.user
        events = Event.objects.filter(user=request.user)
        return render(request, 'event_page.html', {'events': events})


