from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index),
    path('show_task',views.show_task,name='show_task'),
    path("edit_task", views.edit_task,name='edit_task'),
    path('find_task', views.find_task,name='find_task'),   
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    
]