from django.urls import path
from user import views 
urlpatterns = [
    path('admindash', views.admindash, name="admindash"),
    path('edit/<int:p_id>',views.edit, name="edit"),
    path('update/<int:p_id>',views.update, name="update"),
    path('delete/<int:p_id>',views.delete, name="delete")
]