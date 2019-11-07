from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
import pip


def daninstall(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


try:
    import requests
except:
    daninstall(requests)
    import requests

# Create your views here.
from webel.forms import SignUpForm, LoginForm

from webel.forms import ContactForm


def index(request):
    return render(request, 'base.html')


def sign_up(request):
    return render(request, 'b_register.html')


def signup(request):
    message = "nothing"

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
            print(form.errors)
            message = form.errors
    else:
        form = SignUpForm()
    return render(request, 'b_register.html', {'form': form, 'message': message})


def login_view(request):
    message = 'nothing'

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                message = 'invalid'
    else:
        form = LoginForm()

    return render(request, 'b_login.html', {'form': form, 'message': message})


def contact(request):
    sent = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = form.cleaned_data['title']
            message = form.cleaned_data['text']

            daniurl = "https://azmabepors.com/action/webel"

            postdata = {
                'title': subject,
                'text': message
            }

            r = requests.post(daniurl, data=postdata)

            sent = True

            # return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'sent': sent})
