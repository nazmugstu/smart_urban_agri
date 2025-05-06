from django.urls import path
from django.shortcuts import redirect
from . import views

def redirect_to_home(request):
    return redirect('home')

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('home/', redirect_to_home, name='home_redirect'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/signin/', views.signin, name='signin'),
    path('dashboard/signup/', views.signup, name='signup'),
    path('dashboard/signout/', views.signout, name='signout'),
    path('dashboard/control/', views.control, name='dashboard_control'),
    path('dashboard/analytics/', views.analytics, name='analytics'),
    path('devices/', views.control, name='control'),
    path('community/', views.community, name='community'),
]