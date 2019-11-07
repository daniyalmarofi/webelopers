from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.sign_up),
    path('login', views.login),
]
