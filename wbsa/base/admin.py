from django.contrib import admin
# from django.contrib.auth.admin import Us
from .models import User, SoftwareLicenseKey

admin.site.register(User)
admin.site.register(SoftwareLicenseKey)
