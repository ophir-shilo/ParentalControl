from django.shortcuts import render
from django.http import HttpResponse
from .models import KeyLog, ScreenRecord, HistoryFile
from children.models import BlockedUrl
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os.path
import sqlite3



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


@csrf_exempt
def gethistory(request):
    user = User.objects.filter(username=request.POST.get('user')).first()
    if user is None:
        k = HistoryFile(history=request.FILES.get('history'))
    else:
        k = HistoryFile(history=request.FILES.get('history'), user=user)
    k.save()
    db_path = settings.MEDIA_ROOT + "\\histories\\" + str(user) + ".db"
    print(db_path)
    if os.path.exists(db_path):
        db = sqlite3.connect(db_path)
        cursor = db.cursor()
        select_max_statement = '''SELECT max(visit_time) FROM history;'''
        cursor.execute(select_max_statement)
        max_time = cursor.fetchall()[0][0]
        print(max_time)
        select_statement = '''SELECT urls.url, urls.title, visits.visit_time FROM urls, visits WHERE urls.id = visits.url AND visits.visit_time>''' + str(max_time) + ''' ORDER BY visits.visit_time;'''
    else:
        # create db
        db = sqlite3.connect(db_path)
        cursor = db.cursor()
        create_table_statement = '''CREATE TABLE history ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [url] LONGVARCHAR, [title] LONGVARCHAR, [visit_time] INTEGER);'''
        cursor.execute(create_table_statement)
        db.commit()
        select_statement = '''SELECT urls.url, urls.title, visits.visit_time FROM urls, visits WHERE urls.id = visits.url ORDER BY visits.visit_time;'''
    input_db_path = settings.MEDIA_ROOT + "\\" + str(k.history)
    input_db = sqlite3.connect(input_db_path)
    cursor2 = input_db.cursor()
    cursor2.execute(select_statement)
    results = cursor2.fetchall()
    # write the data
    cursor.executemany('''INSERT INTO history (url, title, visit_time) VALUES(?,?,?);''', results)
    db.commit()
    print(input_db_path)
    os.remove(input_db_path)
    k.delete()
    return HttpResponse('success ' + str(user))


def blocked_urls(request):
    user = User.objects.filter(username=request.GET.__getitem__('user')).first()
    if user is None:
        return HttpResponse('error')
    else:
        urls = BlockedUrl.objects.filter(user=user)
        urls_string = "ok"
        for url in urls:
            urls_string = urls_string + "  " + url.url.replace(' ', '') # split with two spaces.
        return HttpResponse(urls_string)
