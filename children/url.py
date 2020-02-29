from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='child-home'),
    path('about/', views.about, name='child-about'),
]
