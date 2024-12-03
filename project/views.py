from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . models import Room, Topic, Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . forms import RoomForm
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username', '').lower()
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
    context = {'page': page}
    return render(request, 'project/login_register.html', context)

def logoutUser(request):
    logout(request) # We don't need to provide the user cuz it's just deleting the token.
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =  form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error has occured during registration, try again")
    context = {'form': form} 
    return render(request, 'project/login_register.html', context)

def room(request, pk):
    rooms = Room.objects.all()
    room = None
    for i in rooms:
        if i.id == int(pk):
            room = i
            break
    room_messages = room.message_set.all().order_by('-created')
    if request.method == "POST":
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
    context = {'room': room, 'room_messages': room_messages}
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

@login_required(login_url='login') # I stil need to figure it out in the new version
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form }
    return render(request, 'project/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host: # the request has the user and the room has the host don't miss it
        return HttpResponse("You are not allowed here")
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form }
    return render(request, 'project/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host: # the request has the user and the room has the host don't miss it
        return HttpResponse("You are not allowed here")
    if request.method == 'POST':
        room.delete()
    return render(request, 'project/delete.html', {'obj':room})