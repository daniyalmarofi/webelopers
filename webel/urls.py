from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('', views.index),
    path('register', views.signup),
    path('login', views.login_view),
    path('register', views.sign_up),
    path('login', views.login),
    path('contact', views.contact),
]
