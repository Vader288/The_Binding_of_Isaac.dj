from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('страница приложения humster' )

def category(request):
    return HttpResponse('<h1>страница хомячки по категориям</h1>' )