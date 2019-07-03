from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group


class Project(models.Model):
    name = models.CharField(max_length = 250)
    start = models.DateField(verbose_name = 'Start Date')
    end = models.DateField(verbose_name = 'End Date')
    # status
    assigned_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank = True,
        related_name = 'projects'
    )
    assigned_groups = models.ManyToManyField(
        Group,
        blank = True,
        related_name = 'projects',
    )
    progress = models.PositiveSmallIntegerField(default = 0, editable = False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'created_projects',
        editable = False,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'updated_projects',
        editable = False,
    )
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created', 'name')
