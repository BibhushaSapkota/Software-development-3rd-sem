import imp
from django.shortcuts import render
from customer.models import Customer
from customer.forms import CustomerForm
from django.shortcuts import redirect
from user.models import *
from user.forms import *

# Create your views here.


def admindash(request):
    customers=Customer.objects.raw('select * from customer')
    return render(request,"admin/admindash.html",{'customers':customers})

def edit(request,p_id):
    try:
       customer=Customer.objects.get(customer_id=p_id)
       return render(request, "admin/edit.html", {'customer':customer})
    except:
       print("No Data Found")
    return redirect("/user/admindash")

def update(request,p_id):
    customer=Customer.objects.get(customer_id=p_id)
    form=CustomerForm(request.POST, instance=customer)
    form.save()
    return redirect ("/user/admindash")

def delete(request,p_id):
    customer=Customer.objects.get(customer_id=p_id)
    customer.delete()
    return redirect ("/user/admindash")

def adduser(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/user/userinfo")
            except:
                print("validation failed")
    else:
        form=UserForm()
        print("invalid")
    return render(request, "user/adduser.html",{'form':form})


def edituser(request,p_id):
    try:
       user=User.objects.get(id=p_id)
       return render(request, "user/edituser.html", {'users':user})
    except:
       print("No Data Found")
    return redirect("/user/userinfo")


def updateuser(request,p_id):
    user = User.objects.get(id=p_id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        try:
           form. save()
           return redirect("/user/userinfo")
        except:
           print("validation failed")
    return render(request, "user/edituser.html", {'users':user})

def deleteuser(request,p_id):
    try:
       user=User.objects.get(id=p_id)
       user.delete()
    except:
        print("No data Found")
    return redirect("/user/userinfo")


