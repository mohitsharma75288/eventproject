from django.shortcuts import render

# Create your views here.
from .models import event
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def input(request):
    if request.method == 'POST':
        seats = request.POST["seats"]
        dsOb = event()

        dsOb.seats = seats

        dsOb.save()

    context = {}
    return render(request, 'core/input.html', context)


def show(request):
	latest=event.objects.latest('id')
	print(latest)
	context={'latst':latest}
	return render(request, 'core/temp.html', context)


def core(request):
    context={}
    return render(request, 'core/core.html', context)
