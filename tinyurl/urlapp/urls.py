from django.urls import path # type: ignore
from . import views

app_name = 'urlapp'

urlpatterns = [
    path("",views.shorturl, name='home'),
    path('urls/list/', views.original_url, name='url_list'),
    # path('<str:short_url>/', views.resolve_url, name='resolve_url'),
    # path('<str:org_url>/shorturl', views.shorturl, name='shorturl'),
]