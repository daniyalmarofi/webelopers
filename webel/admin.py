from django.contrib import admin

from webel.forms import UploadFileForm
from .models import Contact, Course, UserProfile

# Register your models here.
admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(UserProfile)
