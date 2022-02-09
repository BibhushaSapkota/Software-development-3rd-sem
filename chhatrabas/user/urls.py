from django.urls import path
from user import views 
urlpatterns = [
<<<<<<< HEAD
    path('admindash', views.admindash, name="admindash"),
    path('edit/<int:p_id>',views.edit, name="edit"),
    path('update/<int:p_id>',views.update, name="update"),
    path('delete/<int:p_id>',views.delete, name="delete")
=======
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
>>>>>>> 3a36dd477292d440b7c32cda54324876d84465ff
]