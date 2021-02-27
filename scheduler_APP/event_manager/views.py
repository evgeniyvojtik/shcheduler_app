from datetime import date
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from event_manager.models import Event, CountryHoliday
from event_manager.serializers import EventSerializer, GroupByDayEventSerializer, HolidaySerializer


class CreateEvent(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Todays_Events(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        events = Event.objects.filter(user_id=self.request.user.id)
        today_events = events.filter(date_time_start__date=date.today())
        return today_events


class Date_Events(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        chosen_date = self.request.POST.__getitem__('date')
        events = Event.objects.filter(user_id=self.request.user.id)
        date_events = events.filter(date_time_start__date=chosen_date)
        return date_events


class YourMonthEvents(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GroupByDayEventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        events = Event.objects.filter(
            user_id=self.request.user.id,
            date_time_start__month=date.today().month
        )
        days = events.order_by('date_time_start').values('date_time_start').distinct()
        for day in days:
            events_in_day = [
                f'{e.event}: {e.date_time_start.date()} с {e.date_time_start.time()} по {e.date_time_finish.time()}'
                for e in Event.objects.filter(date_time_start=day['date_time_start'])
            ]
            day['event'] = events_in_day
        return days


class YourHolidays(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = HolidaySerializer
    queryset = CountryHoliday.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["holiday_begin"]
    filter_fields = ('holiday_begin', 'holidays')

    def get_queryset(self):
        holidays = CountryHoliday.objects.filter(
            country=self.request.user.country_id
        )
        return holidays
