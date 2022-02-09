from django.shortcuts import render,redirect
from hostel.forms import HostelForm,ReviewForm

# Create your views here.
def hostelbook(request):
    if request.method == "POST":
        print(request.POST)
        form = HostelForm(request.POST)
        form.save()
        return redirect("/customer/hostelprofile")
    else:
        form = HostelForm()
def hostelreview(request):
    if request.method=="POST":
        form=ReviewForm(request.POST)
        form.save()
        
    return render(request,"hostel/review.html")