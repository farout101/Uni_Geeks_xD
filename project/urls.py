from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("roomlist/", views.rooms_list),
    path("room/<str:pk>", views.room, name="room"),
]
