from django.urls import path, include

from authentication_app.views import RegisterAPI, CreateToken, LoginUser
from event_manager.views import YourHolidays, CreateEvent, YourMonthEvents, Todays_Events, Date_Events

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('create_token', CreateToken.as_view(), name='create-token'),
    path('loginuser', LoginUser.as_view()),
    path('holidays', YourHolidays.as_view()),
    path('addevent', CreateEvent.as_view(), name='create-event'),
    path('yourmonthevents', YourMonthEvents.as_view()),
    path('date_events', Date_Events.as_view()),
    path('todays_events', Todays_Events.as_view()),
]