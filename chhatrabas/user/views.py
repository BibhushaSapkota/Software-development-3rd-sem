import imp
from django.shortcuts import render
from customer.models import Customer
from customer.forms import CustomerForm
from django.shortcuts import redirect
from user.models import *
from user.forms import *
from authenticate import *
# Create your views here.

@Authentication.valid_user
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
    return redirect ("/")

@Authentication.valid_user
def delete(request,p_id):
    customer=Customer.objects.get(customer_id=p_id)
    customer.delete()
    return redirect ("/user/admindash")

@Authentication.valid_user
def userinfo(request):
    if(request.method=="POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if ('next' in request.POST):
             page=page+1
        tempOffSet = page - 1
        offset=tempOffSet*4
        print(offset)
    else:
        offset=0
        page=1
    users=User.objects.raw("select * from users limit 4 offset % s",[offset])
    pageItem=len(users)
    return render(request,"admin/user.html",{'users':users,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def adduser(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/user/viewuser")
            except:
                print("validation failed")
    else:
        form=UserForm()
        print("invalid")
    return render(request, "admin/adduser.html",{'form':form})


@Authentication.valid_user
def edituser(request,p_id):
    try:
       user=User.objects.get(id=p_id)
       return render(request, "admin/edituser.html", {'users':user})
    except:
       print("No Data Found")
    return redirect("/user/viewuser")


def updateuser(request,p_id):
    user = User.objects.get(id=p_id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        try:
           form. save()
           return redirect("/user/viewuser")
        except:
           print("validation failed")
    return render(request, "admin/edituser.html", {'users':user})


def deleteuser(request,p_id):
    try:
       user=User.objects.get(id=p_id)
       user.delete()
    except:
        print("No data Found")
    return redirect("/user/viewuser")