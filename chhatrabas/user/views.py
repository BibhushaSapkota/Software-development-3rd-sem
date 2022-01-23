import imp
from django.shortcuts import render
from customer.models import Customer
from customer.forms import CustomerForm
from django.shortcuts import redirect


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