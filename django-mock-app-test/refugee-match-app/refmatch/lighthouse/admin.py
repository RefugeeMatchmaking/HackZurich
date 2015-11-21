from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = ['last_name', 'first_name']


admin.site.register(User, UserAdmin)

# Register your models here.
