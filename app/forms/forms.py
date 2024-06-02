from django import forms
from ..models import Doctor, Office
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class DoctorSignupForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ('email', 'names', 'first_lastname', 'second_lastname', 'phone_number', 'date_of_birth', 'main_office_address', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError("The email field is required.")
        return email

class OfficeCreationForm(forms.ModelForm):
    class Meta:
        model = Office
        exclude = ['is_deleted']

class OfficeUpdateForm(forms.ModelForm):


    class Meta:
        model = Office
        fields = '__all__'