
from django.urls import path
from customer import views 
urlpatterns = [
    path('register', views.register),
    path('login',views.login_redirect),
    path('dashboard',views.dashboard),
    path('blog',views.blog),
    path('contact',views.contact),
    path('hostel',views.hostel),
    path('hostelprofile',views.hostelprofile),
    path('home',views.home),
    path('userprofile',views.userprofile),
    path('signout',views.signout)
]
