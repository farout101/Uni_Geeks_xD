from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("roomlist/", views.home),
    path("room/<str:pk>", views.room, name="room"),
]
