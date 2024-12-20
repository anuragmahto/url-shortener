# Create your views here.
import hashlib
from django.http import JsonResponse, HttpResponse # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.template import loader # type: ignore
from .models import URLstore, DomainCounter

def shorturl(request):
    context = {}
    if request.method == 'POST':
        print(type(request.POST))
        org_url = request.POST.get('input_data', '')
        base_url = "http://shurl/"
    
        existing_url = URLstore.objects.filter(original_url=org_url).first()
        if existing_url:
            context['shorturl'] = existing_url.short_url
            context['orgurl'] = existing_url.original_url
            domain_count(org_url)
            top3Domain = DomainCounter.objects.order_by('-count')[:3]
            if(top3Domain):
                context['mostVisited'] = top3Domain
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
        domain_count(org_url)
        context['shorturl'] = short_url
        context['orgurl'] = org_url
    top3Domain = DomainCounter.objects.order_by('-count')[:3]
    if(top3Domain):
        context['mostVisited'] = top3Domain
    return render(request, 'home.html', context)


def domain_count(org_url):
    split_url = org_url.split('/')
    domain = split_url[2]
    existing_domain = DomainCounter.objects.filter(domain_name= domain).first()
    print(existing_domain)
    if(existing_domain):
        # Increment the count
        existing_domain.count += 1
        existing_domain.save()
        return
    domain_obj = DomainCounter(
        domain_name = domain,
        count = 1
    )
    domain_obj.save()