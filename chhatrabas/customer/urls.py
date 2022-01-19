
from django.urls import path
from customer import views 
urlpatterns = [
    path('register', views.register),
<<<<<<< HEAD
    path('login',views.login),
=======
    path('dashboard',views.dashboard),
    path('blog',views.blog),
    path('contact',views.contact),
    path('hostel',views.hostel),
>>>>>>> 26375fd35f59fc9f32a0cb78c6be487058b6157b
]