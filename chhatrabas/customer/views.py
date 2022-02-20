
from email.message import Message
from telnetlib import AUTHENTICATION
from django.shortcuts import redirect, render
from authenticate import Authentication
from customer.forms import CustomerForm, BillingForm,ContactForm
from hostel.forms import *
from customer.models import Customer
from customer.models import Billing
from hostel.models import Hostel
from django.contrib import auth
from django.contrib.auth import login,logout
from user.models import *
from user.forms import *
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        username=request.POST['username']
        if Customer.objects.filter(username=username).exists():
            messages.error(request,'Username already exists')
        else:
            form = CustomerForm(request.POST)
            form.save()
            return redirect("/login")
    else:
        print("invalid")
        form = CustomerForm()
    return render(request, "customer/registration.html")



def login_redirect(request):
    if request.method=='POST':
        print(request)
        username=request.POST["username"]

        password=request.POST["password"]
        try:
            user=User.objects.get(username=username,password=password)
            if user is not None:
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password'] 
                return redirect('/user/admindash')
            
        except:
            try:
                customer=Customer.objects.get(username=username,password=password)
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password']
                request.session['customer_id']=customer.customer_id
                return redirect ('/')
            except:
                messages.error(request, 'Invalid credentials') 
                return redirect("/login")
    else:
        form=CustomerForm()
        print("invalid")
    return render(request,"customer/signin.html",{'form':form}) 



def signout(request):
    request.session.clear()
    return redirect("/")


def home(request):
    return render(request,"customer/home.html")

# def dashboard(request):
#     return render(request,"customer/dashboard.html")

def blog(request):
    return render(request,"Blog.html")

def contact(request):
    print(request)
    if request.method=="POST":
        print("hello")
        form=ContactForm(request.POST)
        print(form)
        form.save()
        messages.info(request,"your message has been submitted")
    return render(request,"contact.html")
    



def billing(request,h_id):
    hostel=Hostel.objects.get(hostel_id=h_id)
    print(hostel)
    if request.method=="POST":
        form=BillingForm(request.POST)
        print(form)
        form.save()

    return render(request,"customer/billing.html",{'hostel':hostel})


def bill(request):
    print(request)
    if request.method=="POST":
        form=BillingForm(request.POST)
        print(form)
        form.save()

    return redirect("/userprofile")

@Authentication.valid_customer
def hostel(request):
    customers=Customer.objects.raw('select * from customer')
    return render(request,"hostel/pagination.html",{'customers':customers})

@Authentication.valid_customer
def hostelprofile(request):
    return render(request,"hostel/profile.html")

@Authentication.valid_customer
def userprofile(request):
    hostels=Hostel.objects.filter(customer_id = request.session['customer_id'])
    bills=Billing.objects.filter(customer_name=request.session['username'])
    users=Customer.objects.get(username=request.session['username'])
    return render(request,"customer/userprofile.html",{'users':[users],'hostels':hostels,'bills':bills})

def delete(request,h_id):
    hostel=Hostel.objects.get(hostel_id=h_id)
    hostel.delete()
    return redirect ("/userprofile")


def date_update(request,h_id):
    print(h_id)
    hostel=Hostel.objects.get(hostel_id=h_id)
    form=HostelupdateForm(request.POST, instance=hostel)
    form.save()
    return redirect ("/userprofile")

