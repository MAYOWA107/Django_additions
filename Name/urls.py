from django.urls import path

from . import views


urlpatterns = [
    path('', views.Full_name, name = 'home'),
    path('division', views.Division, name = 'division'),
]