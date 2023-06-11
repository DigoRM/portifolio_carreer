from django.contrib import admin
from .models import Course, Customer, Framework, ProgrammingLanguage, Project, Category, Update

# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Update)
admin.site.register(Framework)
admin.site.register(ProgrammingLanguage)
admin.site.register(Customer)
admin.site.register(Course)
