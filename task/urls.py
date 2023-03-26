from django.urls import path
from . import views

urlpatterns = [
    path('',views.task,name="home"),
    path('addtask',views.addTask,name="addtask"),
    path('update/<str:pk>',views.updateTask,name="updatetask"),
    path('delete/<str:pk>',views.deleteTask,name="deletetask"),
]
