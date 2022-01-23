
from django.urls import path
from customer import views 
urlpatterns = [
    path('register', views.register),
    path('login',views.login_redirect),
    path('dashboard',views.dashboard),
    path('blog',views.blog),
    path('contact',views.contact),
    path('hostel',views.hostel),
    path('home',views.home),
    path('userprofile',views.userprofile),
]
<<<<<<< HEAD

=======
>>>>>>> 27ecd546c881636b0578ece5b2493513ba529ece
