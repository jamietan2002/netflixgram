from django.urls import path
from .views import index, profile_list, profile, my_watchlist, data, my_network, login_page
from . import views

urlpatterns = [
    path('api/', index, name='index'),
    path('my_network/', my_network, name='my_network'),
    path('my_watchlist/', my_watchlist, name='my_watchlist'),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path('data/', data, name='data'),
    ]