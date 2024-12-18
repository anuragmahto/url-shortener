# Create your views here.
import hashlib
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import URLstore

url_mapping = {}

def shorturl(org_url):
    base_url = "http://shurl/"
    hash_value = hashlib.md5(org_url.encode()).hexdigest()[:6]
    short_url = base_url + hash_value
    url_mapping[short_url] = org_url
    return short_url

def extended_url(short_url):
    return url_mapping.get(short_url)

def home(request):
    if request.method == "POST":
        org_url = request.POST.get('org_url')
        if org_url:
            short_url = shorturl(org_url)
            return render(request, 'home.html', {
                'short_url': short_url,
                'org_url': org_url
            })
    return render(request, 'home.html')

def resolve_url(request, short_url):
    org_url = extended_url(f"http://shurl/{short_url}")
    if org_url:
        return JsonResponse({'original_url': org_url})
    return JsonResponse({'error':'URL not found'}, status=404)

def index(self):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login_view(request):
    return render(request, 'login.html')

def original_url(request):
    obj_url = URLstore.objects.all()
    return render(request, obj_url)