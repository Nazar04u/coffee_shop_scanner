from django.contrib.auth import authenticate
from django.apps import apps

from django import forms
User = apps.get_model('custom_user', "User")
class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': "First name",
            'id': 'form3Example1cg'
        })
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': "Last name",
            'id': 'form3Example1cg'
        })
    )

    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "form-control form-control-lg",
            'placeholder': 'Email',
            'id': "form3Example3cg",
        }),
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg",
            'placeholder': 'Password',
            'id': "form3Example4cg",
        }),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg",
            'placeholder': 'Repeat Password',
            'id': "form3Example4cdg",
        }),
    )
    agreement = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input me-2',
            'id': 'form2Example3cg'
        })
    )

    def clean(self):
        print(self.cleaned_data)
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("passwords dont match")
        if not self.cleaned_data['agreement']:
            raise forms.ValidationError('Need to aggree with terms of use')

    def save(self, commit=True):
        print(self.cleaned_data)
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        user.save()
        return user


class SignInForm(forms.Form):
    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "form-control form-control-lg",
            'placeholder': 'Email',
            'id': "form3Example3cg",
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg",
            'placeholder': 'Password',
            'id': "form3Example4cg",
        }),
    )