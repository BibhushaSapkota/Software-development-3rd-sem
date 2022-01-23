
from django.shortcuts import redirect, render
from customer.forms import CustomerForm
from customer.models import Customer
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
        try:
            user=Customer.objects.get(username=username,password=password)
            login(request,user)
            request.session['username']=request.POST['username']
            return redirect ('/customer/home')
        except:
            admin=auth.authenticate(request,username=username,password=password)
            if admin is not None:
                return redirect('/user/admindash')
            return render("/customer/login")

        # if user is not None:
            
        # elif admin is None:
            

        # else:
        #    return render("/customer/login")
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
    return render(request,"hostel/pagination.html")

def userprofile(request):
   
    users=Customer.objects.get(username=request.session['username'])
    return render(request,"customer/userprofile.html",{'users':[users]})
    

