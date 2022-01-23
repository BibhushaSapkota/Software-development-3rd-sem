
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

def dashboard(request):
    return render(request,"customer/dashboard.html")

def blog(request):
    return render(request,"Blog.html")

def contact(request):
    return render(request,"contact.html")

def hostel(request):
    customers=Customer.objects.raw('select * from customer')
    return render(request,"hostel/pagination.html",{'customers':customers})

def hostelprofile(request):
    return render(request,"hostel/profile.html")