from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'border p-2 rounded'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'border p-2 rounded'}))
    age = forms.IntegerField(label="Age", widget=forms.NumberInput(attrs={'class': 'border p-2 rounded'}))

    class Meta:
        model = Student
        fields = ['name', 'email', 'age']
