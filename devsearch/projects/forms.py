from django import forms
from django.forms import  ModelForm
from django.forms.fields import Field
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']