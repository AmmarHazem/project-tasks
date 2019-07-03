from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

from projects.models import Project


class Task(models.Model):
    name = models.CharField(max_length = 300)
    note = models.TextField(blank = True)
    start = models.DateField(verbose_name = 'Start Date')
    end = models.DateField(verbose_name = 'End Date')
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'tasks')
    assigned_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'assigned_tasks',
        blank = True,
    )
    assigned_groups = models.ManyToManyField(
        Group,
        related_name = 'assigned_groups',
        blank = True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'created_tasks',
        editable = False,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'updated_tasks',
        editable = False,
    )
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created', 'name')
