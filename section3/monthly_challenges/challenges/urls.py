from django.urls import path  # Required to define URL paths
from . import views  # Import views from the same app folder

urlpatterns = [
    #path("january", views.january),  # Maps the "january/" URL to the index view
    #path("february", views.february),
    #path("march", views.march),
    path("", views.index, name="index"), #/challenges/
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge")
]
