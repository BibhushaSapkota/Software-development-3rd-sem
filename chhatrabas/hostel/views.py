from django.shortcuts import render, redirect
from chhatrabas.customer.models import Customer
from hostel.models import Hostel
from hostel.forms import HostelForm
# Create your views here.
def booking_create(request, customer_id):
    if request.method == "POST":
        form = HostelForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                request.session.clear()
                return redirect("/home/decoration")
            except:
                print("validation failed")
    else:
        form = HostelForm()
        print("invalid")
    customer = Customer.objects.get(id=customer_id)
    return render(request, "hostel/profile.html",
                  {'form': form, 'customer_id': customer_id, 'customer': customer})
        