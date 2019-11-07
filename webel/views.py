from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
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


def loginReq(request):
    return render(request, 'b_login.html')


def contact(request):
    sent = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = form.cleaned_data['title']
            message = form.cleaned_data['text']
            sender = form.cleaned_data['email']

            recipients = ['webe19lopers@gmail.com']
            send_mail(subject, message, sender, recipients)
            sent = True

            # return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'sent': sent})
