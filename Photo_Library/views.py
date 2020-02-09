from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.conf import settings
def login(request):
    return render(request, 'ps.html')


# Create your views here.
def thanks(request):
    return render(request,'thank.html')
def image(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = PhotoForm()
    return render(request, 'thank.html', {'form': form})

def display(request):
    img=Photo.objects.all()
    return render(request, 'image.html', {"img": img, 'media_url': settings.MEDIA_URL})

