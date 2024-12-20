from django.urls import path # type: ignore
from . import views

app_name = 'urlapp'

urlpatterns = [
    path("",views.shorturl, name='home'),
]