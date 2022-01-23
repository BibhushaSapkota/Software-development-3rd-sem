
from django.urls import path
from customer import views 
urlpatterns = [
    path('register', views.register),
    path('login',views.login_redirect),
    path('dashboard',views.dashboard),
    path('blog',views.blog),
    path('contact',views.contact),
    path('hostel',views.hostel),
<<<<<<< HEAD
    path('userprofile',views.userprofile)
    ]

=======
    path('hostelprofile',views.hostelprofile),
    path('home',views.home),
    path('userprofile',views.userprofile),
    path('signout',views.signout)
]
>>>>>>> e2c98b2284994635734c886c8136bccf46b2f9fd
