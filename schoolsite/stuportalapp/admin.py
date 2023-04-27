from django.contrib import admin

# Register your models here.
from .models import Student, Course, Unit

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Unit)