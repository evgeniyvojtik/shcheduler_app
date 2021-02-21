from django.urls import path

from accounts.views import UserCreatApiView

urlpatterns = [
    path('register/',UserCreatApiView.as_view() , name='register'),
]