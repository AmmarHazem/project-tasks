from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Project


# @receiver(pre_save, sender = Project)
# def pre_save_project(sender, instance, *args, **kwargs):
    # calculate progress
    # tasks_progress_total = 0
    # for t in instance.tasks.all():
    #     tasks_progress_total += t.progress
    # instance.progress = tasks_progress_total // instance.tasks.count()
