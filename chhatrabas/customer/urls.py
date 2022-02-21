
from django.urls import path
from customer import views 
urlpatterns = [
<<<<<<< HEAD
    path('',views.home),
    path('register', views.register),
    path('login',views.login_redirect),
    path('blog',views.blog),
    path('contact',views.contact),
    path('hostel',views.hostel),
    path('hostelprofile',views.hostelprofile),
    path('userprofile',views.userprofile),
    path('signout',views.signout),
    path('delete/<int:h_id>',views.delete),
    path('date_update/<int:h_id>', views.date_update),
    path('billing/<int:h_id>',views.billing),
    path('billing',views.bill)
=======
    path('',views.home, name="home"),
    path('register', views.register, name='register'),
    path('login',views.login_redirect,name='login'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('hostel',views.hostel,name='hostel'),
    path('hostelprofile',views.hostelprofile,name='hostelprofile'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('signout',views.signout,name='signout'),
    path('delete/<int:h_id>',views.delete,name='delete'),
    path('date_update/<int:h_id>', views.date_update,name='update'),
    path('billing/<int:h_id>',views.billing,name='bill'),
    path('billing',views.bill,name='billing')

>>>>>>> 8c5528a018731bc390e1a6b959d8e295df79b42d
]
