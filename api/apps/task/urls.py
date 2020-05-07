from django.urls import path
from apps.task import views 

urlpatterns = [
    path('get/all', views.TaskList.as_view(), name='get_all_tasks'),
    path('get/all/filter', views.TaskList.as_view(), name='get_all_tasks_filter'),
    path('delete/all', views.TaskList.as_view(), name='delete_all_tasks'),
    path('new/', views.Task.as_view(), name='register_task'),
    path('get/<int:id>', views.Task.as_view(), name='get_task'),
    path('delete/<int:id>', views.Task.as_view(), name='delete_task'),
    path('edit/<int:id>', views.Task.as_view(), name='edit_task'),
]
