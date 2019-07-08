from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Task
from .forms import TaskForm, TaskFormset
from projects.models import Project


class UpdateTask(UpdateView):
    model = Task

    def post(self, request, *args, **kwargs):
        formset = TaskFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                obj = form.save(commit = False)
                obj.updated_by = request.user
                obj.save()
                form.save_m2m()
            messages.success(request, 'Tasks updated')
        else:
            messages.error(request, 'Error updating tasks')
        return redirect('projects:details', pk = obj.project.id)

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('projects')

    def get_object(self, queryset = None):
        id = self.kwargs.get('pk')
        obj = get_object_or_404(Task, id = id)
        return obj

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        project_id = obj.project.id
        obj.delete()
        return redirect('projects:details', pk = project_id)


class CreateTask(CreateView):
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.created_by = self.request.user
        obj.updated_by = self.request.user
        obj.project = get_object_or_404(Project, id = self.request.POST.get('project_id'))
        obj.save()
        form.save_m2m()
        return redirect('projects:details', pk = obj.project.id)


class ListTask(LoginRequiredMixin, ListView):
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.request.user.assigned_tasks.all()
