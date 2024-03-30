from django.urls import path

from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskDetailView

urlpatterns = [
    path('task_list/', TaskListView.as_view(), name='task-list'),
    path('task_create/', TaskCreateView.as_view(), name='task-create'),
    path('task_delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task_update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task_detail/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
]