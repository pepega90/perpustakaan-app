from django.urls import path
from . import views

urlpatterns = [
	path('admin-profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
	path('admin-edit-profile-page/<int:pk>', views.EditProfileView.as_view(), name='edit_profile'),
	path('password/', views.ChangePasswordView.as_view(), name="password"),
	path('password_success', views.password_success, name="password_success"),
]