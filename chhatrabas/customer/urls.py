
from django.urls import path
from customer import views 
urlpatterns = [
    path('register', views.register),
    path('dashboard',views.dashboard),
]