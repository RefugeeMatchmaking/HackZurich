from django.contrib import admin
from grappelli_nested.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import User, Language

class UserAdmin(admin.TabularInline):
	model = User

admin.site.register(User, UserAdmin)
admin.site.register(Language)
