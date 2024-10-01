from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.signup_view, name='register'),
    path('logout/', views.custom_logout, name="logout"),
    path('sign_in', views.sign_in, name='sign_in'),
]