from django.urls import path
from hostel import views 
urlpatterns = [
    path('hostelbook', views.hostelbook , name="hostelbook"),
    path('review',views.hostelreview, name="review")
]
