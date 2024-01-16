from django.shortcuts import render
from django.views.generic import View, DetailView

class HomeView(View):
    def get(self, reguest):
        return render(reguest, 'basic_app/index.html')



class AppView(View):
    def get(self, reguest):
        page_class = 'app'
        return render(reguest, 'basic_app/app.html', {"page_class": page_class})



class BlogView(View):
    def get(self, reguest):
        page_class = 'blog'
        return render(reguest, 'basic_app/blog.html', {"page_class": page_class})


class ContactView(View):
    def get(self, reguest):
        page_class = 'contact'
        return render(reguest, 'basic_app/contact.html', {"page_class": page_class})


class GuideView(View):
    def get(self, reguest):
        page_class = 'guide'
        return render(reguest, 'basic_app/guide.html', {"page_class": page_class})


class Guide2View(View):
    def get(self, reguest):
        page_class = 'guide2'
        return render(reguest, 'basic_app/guide2.html', {"page_class": page_class})


class PayingView(View):
    def get(self, reguest):
        page_class = 'paying'
        return render(reguest, 'basic_app/paying.html', {"page_class": page_class})


class PricingView(View):
    def get(self, reguest):
        page_class = 'pricing'
        return render(reguest, 'basic_app/pricing.html', {"page_class": page_class})


class ResultsView(View):
    def get(self, reguest):
        page_class = 'result_show'
        return render(reguest, 'basic_app/results.html', {"page_class": page_class})


class Results_DetailView(View):
    def get(self, reguest):
        page_class = 'results_detail'
        return render(reguest, 'basic_app/results_detail.html', {"page_class": page_class})


class WorkView(View):
    def get(self, reguest):
        page_class = 'work'
        return render(reguest, 'basic_app/work.html', {"page_class": page_class})


class Work_DetailView(View):
    def get(self, reguest):
        page_class = 'work_detail'
        return render(reguest, 'basic_app/work_detail.html', {"page_class": page_class})
