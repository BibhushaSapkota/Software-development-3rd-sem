
from django.shortcuts import redirect, render
from customer.forms import CustomerForm, BillingForm,ContactForm
from hostel.forms import *
from customer.models import Customer
from hostel.models import Hostel
from django.contrib import auth
from django.contrib.auth import login,logout
from user.models import *
from user.forms import *
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = CustomerForm(request.POST)
        form.save()
        return redirect("/login")
    else:
        form = CustomerForm()
    return render(request, "customer/registration.html", {'form': form})

# def register(request):
#     print(request)
#     if request.method=="POST":
#         form=CustomerForm(request.POST)
#         print('form')
#         if form.is_valid():
#             try:
#                 print("valid")
#                 form.save()
#                 return redirect ("/customer/login")
#             except:
#                 print("validation failed")

#     else:
#         form=CustomerForm()
#         print("invalid")
#     return render(request,"customer/registration.html",{'form':form})

def login_redirect(request):
    if request.method=='POST':
        print(request)
        username=request.POST["username"]

        password=request.POST["password"]
        try:
            customer=Customer.objects.get(username=username,password=password)
            request.session['username']=request.POST['username']
            request.session['customer_id']=customer.customer_id
            return redirect ('/home')
        except:
            user=User.objects.get(username=username,password=password)
            if user is not None:
                return redirect('/user/admindash')
            return render("/login")
    else:
        messages.error(request, 'Username or password doesnt match')
        form=CustomerForm()
        print("invalid")
    return render(request,"customer/signin.html",{'form':form}) 

# def login_redirect(request):
#     print(request)
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=Customer.objects.get(username=username,password=password)

#         if user is not None:
#             login(request,user)
#             request.session['username']=request.POST['username']
#             request.session['customer_id']=user.customer_id
#             return redirect ('/home')
      
#         else:
#            return render("/login")
#     else:
#         form=CustomerForm()
#         print("invalid")
#     return render(request,"customer/signin.html",{'form':form})

def signout(request):
    request.session.clear()
    return redirect("/")


def home(request):
    return render(request,"customer/home.html")

def dashboard(request):
    return render(request,"customer/dashboard.html")

def blog(request):
    return render(request,"Blog.html")

def contact(request):
    if request.method=="POST":
        form=ContactForm
        form.save()
        messages.info("your message has been submitted")
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

def hostel(request):
    customers=Customer.objects.raw('select * from customer')
    return render(request,"hostel/pagination.html",{'customers':customers})

def hostelprofile(request):
    return render(request,"hostel/profile.html")

def userprofile(request):
    hostels=Hostel.objects.filter(customer_id = request.session['customer_id'])
    users=Customer.objects.get(username=request.session['username'])
    return render(request,"customer/userprofile.html",{'users':[users],'hostels':hostels})

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

