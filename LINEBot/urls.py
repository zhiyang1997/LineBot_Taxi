from django.urls import path
from . import views

urlpatterns = [
    path('driverlogin', views.driverlogin),
    path('ChatBot', views.ChatBot)  #呼叫ChatBot

]

