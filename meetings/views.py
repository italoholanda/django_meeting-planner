from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Meeting, Room


def meetings(request):
    return render(request, "website/meetings.html", {"meetings": Meeting.objects.all()})


def meeting(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(
        request,
        "website/meeting.html",
        {
            "title": meeting.title,
            "start_time": meeting.start_time,
            "duration": meeting.duration,
            "room": meeting.room,
            "date": meeting.date,
        },
    )


def new_meeting(request):
    MeetingForm = modelform_factory(Meeting, exclude=[])
    form = MeetingForm()
    return render(request, "website/new-meeting.html", {"form": form})


def room(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(
        request,
        "website/room.html",
        {"name": room.name, "floor": room.floor, "room_number": room.room_number},
    )


def rooms(request):
    return render(
        request,
        "website/rooms.html",
        {
            "rooms": Room.objects.all(),
        },
    )


def new_room(request):
    RoomForm = modelform_factory(Room, exclude=[])
    form = RoomForm()
    return render(
        request,
        "website/new-room.html",
        {
            "form": form,
        },
    )
