from django.shortcuts import render
from . models import Room

# rooms = [
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'shitty java'},
#     {'id':3, 'name':'useless php'}
# ]

def home(request):
    return render(request, 'project/home.html')

def room(request, pk):
    rooms = Room.objects.all()
    room = None
    for i in rooms:
        if i.id == int(pk):
            room = i
            break
    context = {'room': room}
    return render(request, 'project/room.html', context)

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'project/home.html', context)

def createRoom(request):
    context = {}
    return render(request, 'project/room_form.html', context)