# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(self):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())