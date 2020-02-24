from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('Count/', views.Count, name = 'Count'),
    path('about/', views.about, name= 'about'),
    
]
