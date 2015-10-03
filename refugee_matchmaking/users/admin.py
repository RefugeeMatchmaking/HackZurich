from django.contrib import admin
from .models import User, Language

class LanguageInline(admin.TabularInline):
	model = Language
	extra = 1

class UserAdmin(admin.ModelAdmin):
	readonly_fields = ("submitted", "submission_ip", "email")
	date_hierarchy = 'submitted'
	fieldsets = (
		('User info', {
			'classes': ('grp-collapse grp-open',),
			'fields': ('refugee_or_local', 'first_name', 'last_name', 'location')
		}),
		('Details', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('about', 'occupation', 'gender', 'gender_preference', 'social_media')
		}),
		('Meta', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('submitted', 'submission_ip', 'email', 'picture')
		}),
	)
	inlines = [LanguageInline]

admin.site.register(User, UserAdmin)
admin.site.register(Language)
