from django.contrib import admin
from .models import User, Language

class LanguageInline(admin.TabularInline):
	model = Language
	extra = 1

class UserAdmin(admin.ModelAdmin):
	readonly_fields=('submitted', 'submission_ip')
	model = User
	inlines = [LanguageInline]
	list_display = ('first_name', 'location', 'gender','latitude_longitude')

	#Add some function which cacluates the logitude and lattitude when the admin inputs the data

admin.site.register(User, UserAdmin)
admin.site.register(Language)
