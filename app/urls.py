from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="task_list"),
    path('task_update/<str:key>/', views.updateTask, name="task_update"),
    path('task_delete/<str:key>/', views.deleteTask, name="task_delete")
]
