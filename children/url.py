from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='child-home'),
    path('keylogs/', views.keylogs, name='child-keylogs'),
    path('records/', views.records_year, name='child-records-years'),
    path('records/<int:year>/', views.records_month, name='child-records-months'),
    path('records/<int:year>/<int:month>/', views.records_day, name='child-records-days'),
    path('records/<int:year>/<int:month>/<int:day>/', views.records_hour, name='child-records-hours'),
    path('records/<int:year>/<int:month>/<int:day>/<int:hour>/', views.records, name='child-records'),
    path('history/', views.history, name='child-history'),
    path('blockurl/', views.blockedUrls, name='child-blockurl'),
    path('rkeahdsbgfouv/', views.addUrl, name='add'),
    path('remove/<int:id>/', views.unblockUrl, name='child-unblockurl'),
]
