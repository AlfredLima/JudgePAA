from django import forms

from .models import Submission



class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ('name', 'email', 'registration', 'file')
        labels = {
            'registration': 'Matrícula',
            'file': 'Arquivo',
            'name': 'Nome',
            'email': 'E-mail'
        }
        widgets = {
            'registration': forms.TextInput(
                attrs={'class': 'form-control'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control'}),
            'file': forms.FileInput(
                attrs={'class': 'form-control-file'}
            )
        }