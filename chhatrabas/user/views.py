import imp
from django.shortcuts import render
from customer.models import *
from customer.forms import *
from hostel.models import *
from django.shortcuts import redirect
from user.models import *
from user.forms import *
from authenticate import *
from hostel.models import Reviews
# Create your views here.

@Authentication.valid_user
def admindash(request):
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
    reviews=Reviews.objects.all().count()
    customer=Customer.objects.all().count()
    booking=Billing.objects.all().count()

    customers=Customer.objects.raw("select * from customer limit 4 offset % s",[offset])
    pageItem=len(customers)
    return render(request,"admin/admindash.html",{'customers':customers,'reviews':reviews,'customer':customer,'booking':booking,'page':page,'pageItem':pageItem})


def search(request):
    customers=Customer.objects.filter(username=request.POST['search'])
    count=Customer.objects.count()
    if (count>1):
        return render(request, "admin/search1.html", {'customers': customers})
    return render(request,"admin/search.html",{'customers':customers})


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

@Authentication.valid_user
def review(request):
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
    reviews=Reviews.objects.raw("select * from reviews limit 6 offset % s",[offset])
    pageItem=len(reviews)
    return render(request,"admin/reviews.html",{'reviews':reviews,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def message(request):
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
    messages=Contactus.objects.raw("select * from contact limit 6 offset % s",[offset])
    pageItem=len(messages)
    return render(request,"admin/message.html",{'messages':messages,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def booking(request):
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
    booking=Billing.objects.raw("select * from bill limit 6 offset % s",[offset])
    pageItem=len(booking)
    return render(request,"admin/booking.html",{'bookings':booking,'page':page,'pageItem':pageItem})