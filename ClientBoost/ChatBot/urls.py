from .views import bot
from django.urls import path

urlpatterns = [
  path('bot/', bot, name="bot"),
]
