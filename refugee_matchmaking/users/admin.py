from django.contrib import admin
from .models import User, Language

class LanguageInline(admin.TabularInline):
	model = Language
	extra = 1

class UserAdmin(admin.ModelAdmin):
	readonly_fields=('submitted', 'submission_ip',)
	model = User
	inlines = [LanguageInline]

admin.site.register(User, UserAdmin)
admin.site.register(Language)
