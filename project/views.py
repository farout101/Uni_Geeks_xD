from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . models import Room, Topic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'shitty java'},
#     {'id':3, 'name':'useless php'}
# ]


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")
    
    context = {}
    return render(request, 'project/login_register.html', context)

def logoutUser(request):
    logout(request) # We don't need to provide the user cuz it's just deleting the token.
    return redirect('home')

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
    q = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(description__icontains=q) |
        Q(name__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}    
    return render(request, 'project/home.html', context)

@login_required(Login_required='/login') # I stil need to figure it out in the new version
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form }
    return render(request, 'project/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form }
    return render(request, 'project/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
    return render(request, 'project/delete.html', {'obj':room})