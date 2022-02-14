from django.urls import path
from user import views 
urlpatterns = [
    path('admindash', views.admindash),
    path('edit/<int:p_id>',views.edit),
    path('update/<int:p_id>',views.update),
    path('delete/<int:p_id>',views.delete),
    path('adduser',views.adduser),
    path('viewuser',views.userinfo),
    path('edituser/<int:p_id>',views.edituser),
    path('updateuser/<int:p_id>',views.updateuser),
    path('deleteuser/<int:p_id>',views.deleteuser),
    path('customer_search',views.search),
    path('review',views.review),
    path('message',views.message),
    path('booking',views.booking)
]