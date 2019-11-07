from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.signup),
    path('login', views.loginReq),
]
