from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shaily(request):
    return HttpResponse('<h1>This is first app</h1>')