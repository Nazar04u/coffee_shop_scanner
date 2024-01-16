from django.urls import path
from .views import (HomeView, AppView, BlogView, ContactView, GuideView, Guide2View, PayingView, PricingView,
                    ResultsView, Results_DetailView, WorkView, Work_DetailView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('app/', AppView.as_view(), name='app'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('guide/', GuideView.as_view(), name='guide'),
    path('guide2/', Guide2View.as_view(), name='guide2'),
    path('paying/', PayingView.as_view(), name='paying'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('results/', ResultsView.as_view(), name='results'),
    path('results_detail/', Results_DetailView.as_view(), name='results_detail'),
    path('jobs/', WorkView.as_view(), name='jobs'),
    path('job_detail/', Work_DetailView.as_view(), name='jobs_detail'),
]