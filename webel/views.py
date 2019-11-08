from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
from webel.forms import SignUpForm, LoginForm, EditProfile

from webel.forms import ContactForm


def index(request):
    return render(request, 'base.html')


def signup(request):
    message = []

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:

            if 'password2' in form.errors:
                message.append('password')

            if 'username' in form.errors:
                message.append('username')

            print(form.errors)
            print(message)
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
            message = 'notvalid'
    else:
        form = LoginForm()

    return render(request, 'b_login.html', {'form': form, 'message': message})


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('/')


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


@login_required(login_url='/login')
def profile(request):
    username = request.user.username
    user = User.objects.get(username=username)

    profile = {'username': user.username,
               'first_name': user.first_name,
               'last_name': user.last_name}

    return render(request, 'profile.html', {'profile': profile})


@login_required(login_url='/login')
def panel(request):
    return render(request, 'panel.html')


@login_required(login_url='/login')
def setting(request):
    if request.method == "POST":
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfile(instance=request.user)

    return render(request, 'setting.html', {'form': form})
