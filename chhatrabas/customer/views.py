
from django.shortcuts import redirect, render
from customer.forms import CustomerForm
from hostel.forms import *
from customer.models import Customer
from hostel.models import Hostel
from django.contrib import auth
from django.contrib.auth import login,logout

# Create your views here.
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = CustomerForm(request.POST)
        form.save()
        return redirect("/customer/login")
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
    print(request)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=Customer.objects.get(username=username,password=password)

        if user is not None:
            login(request,user)
            request.session['username']=request.POST['username']
            request.session['customer_id']=user.customer_id
            return redirect ('/customer/home')
      
        else:
           return render("/customer/login")
    else:
        form=CustomerForm()
        print("invalid")
    return render(request,"customer/signin.html",{'form':form})

def signout(request):
    request.session.clear()
    return redirect("/customer/dashboard")


def home(request):
    return render(request,"customer/home.html")

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

def userprofile(request):
    hostels=Hostel.objects.filter(customer_id = request.session['customer_id'])
    users=Customer.objects.get(username=request.session['username'])
    return render(request,"customer/userprofile.html",{'users':[users],'hostels':hostels})

def delete(request,h_id):
    hostel=Hostel.objects.get(hostel_id=h_id)
    hostel.delete()
    return redirect ("/customer/userprofile")

def date_update(request,h_id):
    print(h_id)
    hostel=Hostel.objects.get(hostel_id=h_id)
    form=HostelupdateForm(request.POST, instance=hostel)
    form.save()
    return redirect ("/customer/userprofile")

