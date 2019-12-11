from django.contrib import admin

from .models import Courses
# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
	
	list_display = ['name', 'slug', 'start_date', 'created_at']
	search_fields = ['name', 'slug']


admin.site.register(Courses, CoursesAdmin)