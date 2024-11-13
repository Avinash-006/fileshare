from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Session, File
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
import os

def home(request):
    return render(request, 'share/home.html')

def create_session(request):
    session = Session.objects.create()
    return JsonResponse({'key': session.key})

def join_session(request, key):
    try:
        session = Session.objects.get(key=key)
        files = session.files.all()
        return render(request, 'share/receive.html', {'session': session, 'files': files})
    except Session.DoesNotExist:
        return render(request, 'share/home.html', {'error': 'Invalid session key.'})

@csrf_exempt
def upload_file(request, key):
    session = Session.objects.get(key=key)
    file = request.FILES['file']
    File.objects.create(session=session, file=file)
    return JsonResponse({'status': 'success'})

def get_files(request, key):
    session = Session.objects.get(key=key)
    files = [
        {'name': os.path.basename(file.file.name),
         'url': file.file.url,
         'size': file.file.size // 1024} for file in session.files.all()  # size in KB
    ]
    return JsonResponse(files, safe=False)
