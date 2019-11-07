from django.forms import ModelForm, TextInput

from webel.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'email', 'text']
        widgets = {'title': TextInput(attrs={'name': 'title', 'placeholder': 'عنوان'}),
                   'email': TextInput(attrs={'name': 'email', 'placeholder': 'ایمیل شما'}),
                   'text': TextInput(attrs={'name': 'text', 'placeholder': 'پیام'})
                   }
