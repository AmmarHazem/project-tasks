from django.shortcuts import render
from django.views.generic import ListView

from .models import Task


class TasksListView(ListView):
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.request.user.assigned_tasks.all()
