from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'enrollment_date')  # Show these fields
    search_fields = ('name', 'email')  # Add a search bar
    list_filter = ('age',)  # Add filter options based on age

admin.site.register(Student, StudentAdmin)
