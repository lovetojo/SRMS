
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['unique_identifier']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 15:
            raise forms.ValidationError("Age must be 15 or older.")
        return age
