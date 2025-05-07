from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('community/', views.community, name='community'),
    path('control/', views.control, name='control'),
    path('analytics/', views.analytics, name='analytics'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
]