from django.shortcuts import render

# Create your views here.
from .models import book
from core.models import event
from django.http import HttpResponse

def home(request):
	if request.method=='POST':
		firstname=request.POST["fname"]
		lastname=request.POST["bname"]
		email=request.POST["email"]
		contact=request.POST["contact"]
		
		dsOvj=book()
		
		dsOvj.firstname=firstname
		dsOvj.lastname=lastname
		dsOvj.email=email
		dsOvj.contact=contact
		dsOvj.save()
		t=event.objects.latest('id').seats
		t1=t-1
		dsob=event()
		dsob.seats=t1
		dsob.save()



	context={}
	return render(request, 'home/home.html', context)

