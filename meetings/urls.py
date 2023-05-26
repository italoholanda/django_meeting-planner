from django.urls import path
from .views import meetings, meeting, new_meeting, new_room, rooms, room

urlpatterns = [
    path('', meetings, name='meetings'),
    path('meeting/<int:id>', meeting, name='meeting'),
    path('new-meeting/', new_meeting, name='new-meeting'),
    path('rooms/', rooms, name='rooms'),
    path('room/<int:id>', room, name='room'),
    path('new-room', new_room, name='new-room'), 
]
