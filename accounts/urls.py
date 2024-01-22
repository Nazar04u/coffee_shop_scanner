from django.urls import path
from .views import Sign_UpView, Sign_InView, logout_view, User_Contact_View

urlpatterns = [
    path('sign_up/', Sign_UpView.as_view(), name='sign_up'),
    path('sign_in/', Sign_InView.as_view(), name='sign_in'),
    path('sign_out/', logout_view, name='sign_out'),
    path('contact/', User_Contact_View.as_view(), name='contact')
]