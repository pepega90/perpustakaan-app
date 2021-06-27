from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import EditProfileForm, PassChangeForm
# Create your views here.

class ProfileView(DetailView):
	model = User
	template_name = 'registration/profile.html'
	fields = '__all__'


class EditProfileView(UpdateView):
	model = User
	template_name = 'registration/edit_profile.html'
	form_class = EditProfileForm
	success_url = reverse_lazy('home')


class ChangePasswordView(PasswordChangeView):
	form_class = PassChangeForm
	success_url = reverse_lazy('password_success')
	template_name='registration/change-password.html'

def password_success(req):
	return render(req, 'registration/password_success.html')