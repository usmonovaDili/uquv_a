from django.contrib import admin

from .models import Registration, Course, Category, Teacher, AboutUs

admin.site.register(Registration)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Teacher)
admin.site.register(AboutUs)
