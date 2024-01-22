from django.contrib.auth import authenticate
from django.apps import apps
from .models import User_Unauthorized_Contact_Model, User_Contact_Model
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
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("passwords dont match")
        if not self.cleaned_data['agreement']:
            raise forms.ValidationError('Need to aggree with terms of use')

    def save(self, commit=True):
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


class User_Unauthorized_Contact_Form(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': "Name",
        })
    )

    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "form-control form-control-lg",
            'placeholder': 'Email',
        }),
    )
    subject = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg",
            'placeholder': 'Subject',
        }),
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-outline form-control form-control-lg message',
            'placeholder': "Type your message",
            'rows': '2'
        })
    )

    class Meta:
        model = User_Unauthorized_Contact_Model
        fields = '__all__'


class User_Contact_Form(forms.Form):
    subject = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg",
            'placeholder': 'Subject',
        }),
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-outline form-control form-control-lg message',
            'placeholder': "Type your message",
            'rows': '2'
        })
    )

    class Meta:
        model = User_Contact_Model
        fields = ('subject', 'message')
