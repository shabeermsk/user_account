from django.urls import path
from . import views

app_name ='accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('', views.HomeView.as_view(), name='home'),
]
