
from django.shortcuts import redirect, render
from customer.forms import CustomerForm
from customer.models import Customer

# Create your views here.


def register(request):
    print(request)
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect ("/customer/login")
            except:
                print("validation failed")

    else:
        form=CustomerForm()
        print("invalid")
    return render(request,"customer/registration.html",{'form':form})
  

def login(request):
    print(request)
    if request.method=='POST':
        customer_username=request.POST.get("customer_username")

        customer_password=request.POST.get("customer_password")
        user=Customer.objects.get(customer_username=customer_username,customer_password=customer_password)

        if user is not None:
            return redirect ("/customer/home")
        else:
           print('error')
    else:
        form=CustomerForm()
        print("invalid")
    return render(request,"customer/signin.html",{'form':form})



def dashboard(request):
    return render(request,"customer/dashboard.html")

def blog(request):
    return render(request,"Blog.html")

def contact(request):
    return render(request,"contact.html")

def hostel(request):
    return render(request,"hostel/pagination.html")
