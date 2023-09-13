from django.contrib import admin

from .models import Student, StudentOrganization

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ['first_name','last_name','organization','index']
    
admin.site.register(Student,StudentAdmin)
admin.site.register(StudentOrganization)