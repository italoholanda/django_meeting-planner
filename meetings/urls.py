from django.urls import path
from .views import meetings, meeting, rooms, room

urlpatterns = [
    path('', meetings, name='meetings'),
    path('meeting/<int:id>', meeting, name='meeting'),
    path('rooms/', rooms, name='rooms'),
    path('room/<int:id>', room, name='room'),
]
