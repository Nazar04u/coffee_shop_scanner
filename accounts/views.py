from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignUpForm, SignInForm


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
        print(form.is_valid())
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