from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)

from .models import Task
from .serializers import TaskSerializer


class TaskListView(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset


class TaskDetailView(RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskCreateView(CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateView(UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDeleteView(DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()