from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages

from .forms import ProjectForm, ProjectInlineFormset
from .models import Project


class ProjectListView(PermissionRequiredMixin, ListView):
    permission_required = ('projects.view_project',)
    model = Project
    template_name = 'projects/list.html'
    context_object_name = 'projects'

    def get_context_data(self, *args, **kwargs):
        cxt = super(ProjectListView, self).get_context_data(*args, **kwargs)
        cxt['project_form'] = ProjectForm()
        cxt['update_formset'] = ProjectInlineFormset(instance = self.request.user)
        return cxt

    def get_queryset(self):
        return self.request.user.created_projects.all()

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('tasks:list')
        return HttpResponseRedirect(f'{reverse_lazy("login")}?next={self.request.path}')


class ProjectCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('projects.add_project',)
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')
    template_name = 'projects/list.html'

    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.created_by = self.request.user
        obj.updated_by = self.request.user
        obj.save()
        form.save_m2m()
        messages.success(self.request, f'Project {obj.name} created')
        return redirect(self.success_url)

    def form_invalid(self, form):
        cxt = self.get_context_data()
        cxt['project_form'] = cxt['form']
        cxt['projects'] = Project.objects.all()
        messages.error(self.request, 'Please correct form errors and try again')
        return render(self.request, self.template_name, cxt)

    def handle_no_permission(self):
        return HttpResponseRedirect(f'{reverse_lazy("login")}?next={self.request.path}')


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    model = Project
    permission_required = ('projects.delete_project',)
    success_url = reverse_lazy('project_list')

    def get_success_url(self):
        obj = self.get_object()
        messages.info(self.request, f'Project {obj.name} deleted')
        return super(ProjectDelete, self).get_success_url()


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('projects.change_project',)
    model = Project
    template_name = 'projects/list.html'
    success_url = reverse_lazy('project_list')

    def post(self, request):
        formset = ProjectInlineFormset(request.POST, instance = request.user)
        if formset.is_valid():
            instances = formset.save(commit = False)
            for instance in instances:
                instance.created_by = request.user
                instance.save()
                formset.save_m2m()
            messages.success(request, 'Projects updated')
            return redirect('project_list')
        messages.error(request, 'Error updating projects')
        return redirect('project_list')
