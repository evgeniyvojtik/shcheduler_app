from django.contrib import admin
from django.urls import path, include
from manager.views import MainPage, EventPage

urlpatterns = [
    path('event_page', EventPage.as_view(), name='event_page'),
    path('', MainPage.as_view(), name='the-main-page'),
]

