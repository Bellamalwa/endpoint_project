from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.get_info, name='get_info'),
]

