from .models import Employee, Project, ProjectManagement
from django import forms


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectManagementForm(forms.ModelForm):
    class Meta:
        model = ProjectManagement
        exclude = ('status',)
