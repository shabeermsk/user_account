from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class SignupView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

class HomeView(generic.TemplateView):
    template_name = 'accounts/index.html'
