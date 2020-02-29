from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'children/home.html')


def about(request):
    return HttpResponse('<h1>child about</h1>')
