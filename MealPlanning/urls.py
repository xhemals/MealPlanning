from django.urls import path
from . import views
from django.views.generic import DetailView
from .models import Meal

urlpatterns = [
    path("", views.index, name="index"),
    path("planning/", views.planning, name="planning"),
    path("done/", views.done, name="done"),
    path("meal/<pk>", views.MealView.as_view(), name="meal"),
    path("delete/<pk>", views.DeleteView.as_view(), name="delete"),
]
