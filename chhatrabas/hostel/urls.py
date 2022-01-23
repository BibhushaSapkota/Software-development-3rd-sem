from django.urls import path
from hostel import views
urlpatterns = [
    path('booking/<int:customer_id>', views.create),
]