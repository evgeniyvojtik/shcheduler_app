from django.urls import path, include

from event_manager.views import YourHolidays, CreateEvent, YourMonthEvents, Todays_Events

urlpatterns = [
    path('holidays', YourHolidays.as_view()),
    path('addevent', CreateEvent.as_view(), name='create-event'),
    path('yourmonthevents', YourMonthEvents.as_view()),
    path('todays_events', Todays_Events.as_view()),
]