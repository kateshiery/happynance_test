from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from .models import EmailList

class UserForm(ModelForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password2 = forms.CharField(label= ("Confirm Password"), 
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['email'].required = True

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
        
    #Hash password
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class EmailListForm(ModelForm):
    class Meta:
        model = EmailList
        fields = ["email"]