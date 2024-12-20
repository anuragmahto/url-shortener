from django.contrib import admin
from .models import URLstore, DomainCounter

# Register your models here.
admin.site.register(URLstore)
admin.site.register(DomainCounter)