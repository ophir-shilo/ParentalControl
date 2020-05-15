from django.shortcuts import render, redirect
from django.http import HttpResponse
from send.models import KeyLog, ScreenRecord, HistoryFile
from .forms import BlockedUrlForm
from .models import BlockedUrl
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
import sqlite3
from django.conf import settings
import os

def home(request):
    return render(request, 'children/home.html')


def keylogs(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        'keylogs': KeyLog.objects.filter(user=request.user).order_by('-writeTime')
    }
    return render(request, 'children/keylogs.html', context)


def records_year(request):
    if not request.user.is_authenticated:
        return redirect('login')
    q = ScreenRecord.objects.filter(user=request.user).values('writeTime__year').order_by('-writeTime__year').distinct()
    context = {
        'years': q
    }
    return render(request, 'children/nav.html', context)


def records_month(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    q = ScreenRecord.objects.filter(user=request.user, writeTime__year=year).values('writeTime__month').order_by('-writeTime__month').distinct()
    context = {
        'months': q,
        'year': year
    }
    return render(request, 'children/nav.html', context)


def records_day(request, year, month):
    if not request.user.is_authenticated:
        return redirect('login')
    q = ScreenRecord.objects.filter(user=request.user, writeTime__year=year, writeTime__month=month).values('writeTime__day').order_by('-writeTime__day').distinct()
    context = {
        'days': q,
        'year': year,
        'month': month
    }
    return render(request, 'children/nav.html', context)


def records_hour(request, year, month, day):
    if not request.user.is_authenticated:
        return redirect('login')
    q = ScreenRecord.objects.filter(user=request.user, writeTime__year=year, writeTime__month=month, writeTime__day=day).values('writeTime__hour').order_by('-writeTime__hour').distinct()
    context = {
        'hours': q,
        'year': year,
        'month': month,
        'day': day
    }
    return render(request, 'children/nav.html', context)


def records(request, year, month, day, hour):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        'records': ScreenRecord.objects.filter(user=request.user, writeTime__year=year, writeTime__month=month, writeTime__day=day, writeTime__hour=hour).order_by('-writeTime'),
        'year': year,
        'month': month,
        'day': day,
        'hour': hour
    }
    return render(request, 'children/records.html', context)

def history(request):
    if not request.user.is_authenticated:
        return redirect('login')
    db_path = settings.MEDIA_ROOT + "\\histories\\" + str(request.user.username) + ".db"
    if os.path.exists(db_path):
        db = sqlite3.connect(db_path)
        cursor = db.cursor()
        select_max_statement = '''SELECT datetime(visit_time/1000000-11644473600,'unixepoch'), title, url FROM history ORDER BY visit_time DESC'''
        cursor.execute(select_max_statement)
        results = cursor.fetchall()
        context = {'history': results}
        return render(request, 'children/history.html', context)
    else:
        context = {'history': ''}
        return render(request, 'children/history.html', context)


def blockedUrls(request):
    if not request.user.is_authenticated:
        return redirect('login')
    urls = BlockedUrl.objects.filter(user=request.user).order_by('url')
    form = BlockedUrlForm()
    context = {'urls': urls, 'form': form}
    return render(request, 'children/blockurls.html', context)


@require_POST
def addUrl(request):
    form = BlockedUrlForm(request.POST)
    if form.is_valid():
        url = form.save()
        url.user = request.user
        url.save()
    return redirect('child-blockurl')


def unblockUrl(request, id):
    BlockedUrl.objects.filter(id=id).delete()
    return redirect('child-blockurl')
