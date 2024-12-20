# Create your views here.
import hashlib
from django.http import JsonResponse, HttpResponse # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.template import loader # type: ignore
from .models import URLstore

def shorturl(request):
    context = {}
    if request.method == 'POST':
        print(type(request.POST))
        org_url = request.POST.get('input_data', '')
        base_url = "http://shurl/"
        existing_url = URLstore.objects.filter(original_url=org_url).first()

        existing_url = URLstore.objects.filter(original_url=org_url).first()
        if existing_url:
            context['shorturl'] = existing_url.short_url
            context['orgurl'] = existing_url.original_url
            return render(request, 'home.html', context)

        hash_value = hashlib.md5(org_url.encode()).hexdigest()[:6]
        short_url = base_url + hash_value
        while URLstore.objects.filter(short_url=short_url).exists():
            hash_value = hashlib.md5((org_url + str(hash_value)).encode()).hexdigest()[:6]
            short_url = base_url + hash_value
   
        url_obj = URLstore(
            short_url = short_url,
            original_url = org_url
        )
        url_obj.save()
        context['shorturl'] = short_url
        context['orgurl'] = org_url
    return render(request, 'home.html', context)

def extended_url(short_url):
    try:
        url_obj = URLstore.objects.get(short_url=short_url)
        url_obj.click_count += 1
        url_obj.save()
        return url_obj.original_url
    except URLstore.DoesNotExist:
        return None

def home(request):
    if request.method == "POST":
        org_url = request.POST.get('org_url')
        if org_url:
            try:
                existing_url = URLstore.objects.filter(original_url=org_url).first()
                if existing_url:
                    short_url = existing_url.short_url
                else:
                    short_url = shorturl(org_url)
                
                return render(request, 'home.html', {
                    'short_url': short_url,
                    'org_url': org_url
                })  
            except Exception as e:
                return render(request, 'home.html', {
                    'error':f'Error creating short URL :- {str(e)}'
                })
    return render(request, 'home.html')

def resolve_url(request, short_url):
    full_short_url = f"http://shurl/{short_url}"
    org_url = extended_url(full_short_url)
    if org_url:
        return redirect(org_url)
    return HttpResponse({'URL not found'}, status=404)

def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def original_url(request):
    url_objects = URLstore.objects.all().order_by('-created_at')
    return render(request, 'urls_list.html', {'urls': url_objects})