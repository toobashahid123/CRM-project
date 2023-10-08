from django.contrib import admin
from django.urls import path
from . import views
#from django.views.generic import CreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('record/<int:pk>',views.customer_record, name='record'),
    path('delete_record/<int:pk>',views.delete_record, name='delete_record'),
    path('edit-product/<str:pk>',views.edit_record, name='edit_rec'),
    
]
  