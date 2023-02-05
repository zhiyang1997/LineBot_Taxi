from django.urls import path
from . import views

urlpatterns = [
    path('ChatBot', views.ChatBot)  #呼叫ChatBot
]