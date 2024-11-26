from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello This is home")

def room(request):
    return HttpResponse("This is room page")