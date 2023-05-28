from .views import bot, view_ad
from django.urls import path

urlpatterns = [
  path('bot/', bot, name="bot"),
  path('ad_example/', view_ad, name="view_ad")
]
