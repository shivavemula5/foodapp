from django.urls import path
from foodapp import views

urlpatterns = [
    
    #/food/
    path('',views.index,name='index'),
    
    #/food/id
    path('<item_id>/',views.details,name='details'),
    
    
    
    #food/delete/id
    # path('delete/<item_id>',views.delete,name='delete'),
    #food/edit/1
    # path('edit/<item_id>',views.edit,name='edit'),



]
