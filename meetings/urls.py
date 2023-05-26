from django.urls import path
from .views import welcome, about, detail, rooms, room

urlpatterns = [
    path('', welcome, name='welcome'),
    path('about/', about),
    path('meeting-details/<int:id>', detail, name='detail'),
    path('rooms/', rooms, name='rooms'),
    path('room/<int:id>', room, name='room'),
]
