from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Lets learn python'},
    {'id':2, 'name':'shitty java'},
    {'id':3, 'name':'useless php'}
]

def home(request):
    return render(request, 'project/home.html')

def room(request):
    return render(request, 'room.html', {'rooms':rooms})