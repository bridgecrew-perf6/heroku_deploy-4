from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('welcome home and that is all')