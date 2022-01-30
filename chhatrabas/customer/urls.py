
from django.urls import path
from customer import views 
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register', views.register,name='register'),
    path('login',views.login_redirect,name='login'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact),
    path('hostel',views.hostel),
    path('hostelprofile',views.hostelprofile),
    path('home',views.home),
    path('userprofile',views.userprofile),
    path('signout',views.signout)
]
