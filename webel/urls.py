from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('home', views.index),
    path('', views.index),
    path('register', views.signup),
    path('login', views.loginReq),
    path('register', views.sign_up),
    path('login', views.login),
    path('contact',views.contact),
]
