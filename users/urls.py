
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='logout.html'), name='logout'),
    path('login', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('change_password', auth_views.PasswordChangeView.as_view(
        template_name='change_password.html', success_url=reverse_lazy('users:password_change_done')), name='change_password'),
    path('password_change_done', auth_views.PasswordChangeView.as_view(
        template_name='password_change_done.html'), name='password_change_done'),
]
