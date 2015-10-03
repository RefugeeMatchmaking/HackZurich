from django.contrib import admin

from .models import User, Language

admin.site.register(User)
admin.site.register(Language)
