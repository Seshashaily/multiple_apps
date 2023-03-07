from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sesha(request):
    return HttpResponse('<h2>This is second app</h2>')