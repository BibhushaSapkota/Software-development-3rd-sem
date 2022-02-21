from django.urls import path
from user import views 
urlpatterns = [
    path('admindash', views.admindash,name='admindash'),
    path('edit/<int:p_id>',views.edit,name='edit'),
    path('update/<int:p_id>',views.update,name='update'),
    path('delete/<int:p_id>',views.delete,name='delete'),
    path('adduser',views.adduser,name='adduser'),
    path('viewuser',views.userinfo,name='viewuser'),
    path('edituser/<int:p_id>',views.edituser),
    path('updateuser/<int:p_id>',views.updateuser),
    path('deleteuser/<int:p_id>',views.deleteuser),
    path('customer_search',views.search),
    path('review',views.review,name='review'),
    path('message',views.message),
    path('booking',views.booking)
]