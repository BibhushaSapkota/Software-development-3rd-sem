
from django.http import request
from django.shortcuts import redirect, render
from customer.forms import CustomerForm
from customer.models import Customer

# Create your views here.


def register(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        form.save()
    else: 
        return render(request,"customer/registration.html")
