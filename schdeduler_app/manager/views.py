from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from rest_framework import response, status
from rest_framework.response import Response
from rest_framework.views import APIView

from manager.forms import CustomAuthenticationForm, AddEventForm
from manager.models import Event


class MainPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {}
            events = Event.objects.filter(user=request.user)
            context['events'] = events
            context['form'] = AddEventForm()
            return render(request, 'index.html', context)
        return redirect('login')

class EventPage(View):
    def get(self, request):
        user = request.user
        events = Event.objects.filter(user=request.user)
        return render(request, 'event_page.html', {'events': events})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {'form': CustomAuthenticationForm()})

    def post(self, request):
        user = CustomAuthenticationForm(data=request.POST)
        if user.is_valid():
            login(request, user.get_user())
            return redirect("the-main-page")
        messages.error(request, user.error_messages)
        return redirect('login')

def logout_user(request):
    logout(request)
    return redirect('the-main-page')

class LogoutAPI(APIView):
    def post(self, request):
        logout(request)
        return Response({"success": ("Successfully logged out.")},status=status.HTTP_200_OK)

class AddEvent(View):
    def post(self, request):
        if request.user.is_authenticated:
            aef = AddEventForm(data=request.POST)
            event = aef.save(commit=False)
            event.user = request.user
            event.save()
        return redirect("the-main-page")
