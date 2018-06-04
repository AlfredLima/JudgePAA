from django import forms

from .models import Submission

FIELD_NAME_MAPPING = {
    'registration': 'Matrícula',
    'file': 'Arquivo'
}


class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ('registration', 'file')
        labels = {
            'registration': 'Matrícula',
            'file': 'Arquivo'
        }
        widgets = {
           # 'name': forms.TextInput(
           #     attrs={'class': 'form-control opunitName'}),
        }