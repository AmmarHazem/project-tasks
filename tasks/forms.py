from django import forms
from django.contrib.auth.models import User

from .models import Task
from projects.models import Project

class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
            self.fields[f].widget.attrs['placeholder'] = f
        self.fields['assigned_users'].widget.attrs['class'] += ' select2-multiple'
        self.fields['assigned_groups'].widget.attrs['class'] += ' select2-multiple'
        self.fields['start'].widget.attrs['class'] += ' date-selector'
        self.fields['end'].widget.attrs['class'] += ' date-selector'
        self.fields['start'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['end'].widget.attrs['placeholder'] = 'YYYY-MM-DD'

    class Meta:
        model = Task
        fields = ('name', 'note', 'start', 'end', 'assigned_users', 'assigned_groups')


TaskFormset = forms.inlineformset_factory(
    Project,
    Task,
    TaskForm,
    # fields = ('')
)
