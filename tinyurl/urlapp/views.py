# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(self):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login_view(request):
    return render(request, 'login.html')