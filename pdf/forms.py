from django import forms
from pdf import models

class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = '__all__'
