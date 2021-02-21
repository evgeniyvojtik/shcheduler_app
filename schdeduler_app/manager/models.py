from datetime import timedelta

from django.contrib.auth.models import  User
from django.db import models
import holidays
import datetime


class Country(models.Model):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = "Страны"

    slug = models.SlugField(primary_key=True, verbose_name='slug')
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class Event(models.Model):
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    TYPE_REMIND = [
        ((timedelta(hours=1)), 'За час'),
        ((timedelta(hours=2)), 'За 2 часа'),
        ((timedelta(hours=4)), 'За 4 часа'),
        ((timedelta(days=1)), 'За день'),
        ((timedelta(weeks=1)), 'За неделю'),
    ]

    title = models.CharField(max_length=250)
    date_from = models.DateField(verbose_name='event_start_date')
    start_time = models.TimeField(verbose_name='event starts...')
    date_till = models.DateField(verbose_name='event_end_date')
    end_time = models.TimeField(verbose_name='event_end_time...')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_event')

    def __str__(self):
        return f"Event is {self.title}"


class Holidays(models.Model):
    holiday = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='holiday_date')

