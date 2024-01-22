from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignUpForm, SignInForm, User_Contact_Form, User_Unauthorized_Contact_Form
from .models import User_Unauthorized_Contact_Model, User_Contact_Model
from django.apps import apps

User = apps.get_registered_model('custom_user', "User")

class Sign_InView(View):
    def get(self, request):
        page_class = 'sign_in'
        form = SignInForm()
        return render(request, 'accounts/sign_in.html', context={
            'form': form,
            'page_class': page_class
        })

    def post(self, request):
        page_class = 'sign_in'
        form = SignInForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'accounts/sign_in.html', context={
            'form': form,
            'page_class': page_class
        })


class Sign_UpView(View):

    def get(self, request):
        page_class = 'signup'
        form = SignUpForm()
        return render(request, 'accounts/sign_up.html', context={
            'form': form,
            "page_class": page_class
        })

    def post(self, request):
        page_class = 'signup'
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # ADD method save in forms
            if user is not None:
                login(request, user)
            return redirect('home')
        return render(request, 'accounts/sign_up.html', context={
            'form': form,
            'page_class': page_class
        })


def logout_view(request):
    logout(request)
    return redirect('home')


class User_Contact_View(View):

    def get(self, request):
        page_class = 'contact'
        if request.user.is_authenticated:
            form = User_Contact_Form()
            return render(request, 'accounts/contact.html', context={
                'form': form,
                'page_class': page_class
            })
        else:
            form = User_Unauthorized_Contact_Form()
            return render(request, 'accounts/contact.html', context={
                'form': form,
                'page_class': page_class
            })

    def post(self, request):
        page_class = 'contact'
        if request.user.is_authenticated:
            form = User_Contact_Form(request.POST)
            user = request.user
            if form.is_valid():
                subject = request.POST['subject']
                message = request.POST['message']
                user_message = User_Contact_Model.objects.create(user=user, subject=subject, message=message)
                return redirect('home')
            form = User_Contact_Form()
            return render(request, 'accounts/contact.html', context={
                'form': form,
                'page_class': page_class
            })
        else:
            form = User_Unauthorized_Contact_Form(request.POST)
            user = request.user
            if form.is_valid():
                name = request.POST['name']
                email = request.POST['email']
                subject = request.POST['subject']
                message = request.POST['message']
                user_message = User_Unauthorized_Contact_Model.objects.create(name=name, email=email, subject=subject,
                                                                              message=message)
                return redirect('home')
            form = User_Unauthorized_Contact_Form()
            return render(request, 'accounts/contact.html', context={
                'form': form,
                'page_class': page_class
            })
