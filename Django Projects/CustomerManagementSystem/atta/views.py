from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
# Create your views here.

def index(request):
	allCustomers = Customer.objects.all()
	primeCustomers = Customer.objects.all().order_by('-amount')[:3]
	params = {

			'allCustomers' : allCustomers,
			'primeCustomers' : primeCustomers

	}
	return render(request,'atta/index.html',params)



def updateCustomer(request):
	if request.method == 'POST':
		sno = request.POST.get('clickedCustomerId')
		action = request.POST.get('action')
		name = request.POST.get('name')
		amount = request.POST.get('amount')
		if sno == '' and action == 'insert':
			customer = Customer(name=name,amount=amount)
			customer.save()
		else:
			customer = Customer.objects.filter(sno=sno).first()	
			customer.name = name
			customer.amount	= amount
			customer.save()
		return redirect('/')

	else:
		return HttpResponse('Bad Request')		
