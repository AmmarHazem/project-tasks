from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import User

from .models import Project


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
            self.fields[f].widget.attrs['placeholder'] = f
        # self.fields['assigned_users'].widget.attrs['class'] += ' select2-multiple'
        # self.fields['assigned_groups'].widget.attrs['class'] += ' select2-multiple'
        self.fields['start'].widget.attrs['class'] += ' date-selector'
        self.fields['end'].widget.attrs['class'] += ' date-selector'
        self.fields['end'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['start'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['start'].widget.attrs['id'] = 'id_task_start'
        self.fields['end'].widget.attrs['id'] = 'id_task_end'

    class Meta:
        model = Project
        fields = ('name', 'start', 'end')


ProjectInlineFormset = forms.inlineformset_factory(
    User,
    Project,
    ProjectForm,
    fk_name = 'created_by',
    # fields = ('name', 'start', 'end', 'assigned_users', 'assigned_groups',),
    can_delete = False,
)
