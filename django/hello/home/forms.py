from django import forms
from .models import Student, Employee


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        error_messages = {
            'name': {'required': 'Student name required'},
            'contact': {'required': 'Contact required'},
        }

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')

        if not contact.isdigit():
            raise forms.ValidationError("Only numbers allowed")

        if len(contact) != 10:
            raise forms.ValidationError("Must be 10 digits")

        return contact


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        error_messages = {
            'name': {'required': 'Name is required'},
            'email': {'invalid': 'Enter valid email'},
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age < 18:
            raise forms.ValidationError("Age must be 18+ ⚠️")

        return age