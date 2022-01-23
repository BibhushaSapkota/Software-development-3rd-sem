from django.urls import path
from user import views 
urlpatterns = [
    path('admindash', views.admindash),
    path('edit/<int:p_id>',views.edit),
    path('update/<int:p_id>',views.update),
    path('delete/<int:p_id>',views.delete)
]