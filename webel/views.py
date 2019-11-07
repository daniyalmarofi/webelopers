from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from webel.forms import SignUpForm

from webel.forms import ContactForm


def index(request):
    return render(request, 'base.html')


def sign_up(request):
    return render(request, 'b_register.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print(form.error_messages)
    else:
        form = SignUpForm()
    return render(request, 'b_register.html', {'form': form})


def login(request):

def loginReq(request):
    return render(request, 'b_login.html')


def contact(request):
    form = ContactForm()

    return render(request, 'contact.html', {'form': form})
