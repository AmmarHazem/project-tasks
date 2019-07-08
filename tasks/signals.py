from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Task

actions = {'post_add', 'post_remove'}
@receiver(post_save, sender = Task.assigned_users.through)
def post_save_task(sender, action, instance, created, *args, **kwargs):
    if action in actions:
        project = instance.project
        
