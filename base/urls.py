
from django.contrib import admin
from django.urls import path
from .views import index, RegisterAPI, login_view
from knox import views as knox_views

urlpatterns = [
    path('', index, name='index'),
    path('api/register', RegisterAPI.as_view(), name='register'),
    path('api/login', login_view, name='login'),
    path('api/logout', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
