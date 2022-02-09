
from django.urls import path
from customer import views 
urlpatterns = [
<<<<<<< HEAD
    path('', views.dashboard, name='dashboard'),
    path('register', views.register,name='register'),
    path('login',views.login_redirect,name='login'),
    path('blog',views.blog,name='blog'),
=======
    path('',views.home),
    path('register', views.register),
    path('login',views.login_redirect),
    path('blog',views.blog),
>>>>>>> 3a36dd477292d440b7c32cda54324876d84465ff
    path('contact',views.contact),
    path('hostel',views.hostel),
    path('hostelprofile',views.hostelprofile),
    path('userprofile',views.userprofile),
    path('signout',views.signout),
    path('delete/<int:h_id>',views.delete),
    path('date_update/<int:h_id>', views.date_update),
    path('billing/<int:h_id>',views.billing),
    path('billing',views.bill)

]
