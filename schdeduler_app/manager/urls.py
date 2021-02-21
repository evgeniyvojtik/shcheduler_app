from django.urls import path
from manager.views import MainPage, EventPage, LoginView, AddEvent, logout, logout_user, LogoutAPI

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path("logout_api", LogoutAPI.as_view(), name='logout_api'),
    path('event_page', EventPage.as_view(), name='event_page'),
    path('add_event', AddEvent.as_view(), name='add_event'),
    path('', MainPage.as_view(), name='the-main-page'),
]

# path('logout_user', logout_user, name='logout_user'),