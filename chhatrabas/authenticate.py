from django.shortcuts import redirect
from user.models import User
from customer.models import Customer
from django.contrib import messages
class Authentication:
    def valid_user(function):
        def wrap(request):
            
            try:
                User.objects.get(username=request.session["username"],password=request.session["password"])
                return function(request)
            except:
                print('no authentication')
                messages.warning(request,'Note:Please enter valid email and password')
            return redirect('/login')
        return wrap

    def valid_user_where_id(function):
        def wrap(request,p_id):
            try:
                User.objects.get(username=request.session['username'], password=request.session['password'])
                return function(request,p_id)
            except:
                messages.warning(request, 'Please enter valid email and password')
                return redirect('/login')
        return wrap

    def valid_customer(function):
        def wrap(request):
            try:
                Customer.objects.get(username=request.session["username"],password=request.session["password"])
                return function(request)
            except:
                print('no authentication')
                messages.warning(request,'Note:Please enter valid email and password')
            return redirect('/login')
        return wrap

    def valid_customer_where_id(function):
        def wrap(request,p_id):
            try:
                Customer.objects.get(username=request.session['username'], password=request.session['password'])
                return function(request,p_id)
            except:
                messages.warning(request, 'Please enter valid email and password')
                return redirect('/login')
        return wrap

