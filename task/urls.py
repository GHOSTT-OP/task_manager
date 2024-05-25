# from django.urls import path
# from .views import task_view
# urlpatterns = [
#     path('tasks/', task_view , name = 'tasks') ,
#     path('tasks/<int:pk>/', task_view, name='task-detail'),
# ]
from django.urls import path
from .views import task_view

urlpatterns = [
    path('tasks/', task_view, name='task-list'),
    path('tasks/<int:pk>/', task_view, name='task-detail'),
]


