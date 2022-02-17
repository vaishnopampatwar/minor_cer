from django import forms 
from django.forms import Form
from home.models import ResultAnalysis


class FileForm(forms.ModelForm):
    class Meta:
        model= ResultAnalysis
        fields= ["course_id", "result_file"]
