from django.urls import path # type: ignore
from . import views

app_name = 'urlapp'

urlpatterns = [
    path("",views.home, name='home'),
    path('urls/', views.original_url, name='url_list'),
    path('<str:short_url>/', views.resolve_url, name='resolve_url'),
]