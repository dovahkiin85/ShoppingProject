from django.contrib import admin
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
