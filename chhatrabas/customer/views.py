
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
        user=Customer.objects.get(username=username,password=password)

        if user is not None:
            login(request,user)
            request.session['username']=request.POST['username']
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
    users=Customer.objects.get(username=request.session['username'])
    return render(request,"customer/userprofile.html",{'users':[users]})
    

