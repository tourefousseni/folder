
from django.shortcuts import render
#from django.templates import TestForm
from django.http import HttpResponse
from django.views import View
from k import views, index



def index(request):
    return HttpResponse("welcome to kalaliso")