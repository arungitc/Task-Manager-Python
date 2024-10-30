from django import forms
from .models import Report
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
# ['user','subject', 'head_under_project_website', 'date' ,'email', 'pdf_link', 'Name_of_Institutes']
        widgets = {
            'user' : forms.Select(attrs=
                                    {'class': 'form-control  fs-6'}),
            'subject' : forms.Textarea(attrs=
                                       
                                    {'class': 'form-control fs-6',
                                    'rows': 4, 'cols': 15}),
            'docId' : forms.TextInput(attrs=
                                    {'class': 'form-control fs-6'}),
                                 
            'head_under_project_website' : forms.TextInput(attrs=
                                    {'class': 'form-control '}),
            'date' : forms.DateInput(attrs=
                                    {'type': 'date', 'class': 'form-control w-auto'}),
            'email' : forms.TextInput(attrs=
                                    {'class': 'form-control '}),
            'pdf_link' : forms.TextInput(attrs=
                                    {'class': 'form-control'}),
            'other_pdf' : forms.TextInput(attrs=
                                          {'class': 'form-control'}),
            'Name_of_Institutes' : forms.Select(attrs=
                                    {'class': 'form-control'}),
        }



# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2' )


class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data



