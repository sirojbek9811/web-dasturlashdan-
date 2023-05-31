from django.contrib import admin

from .models import Course, Opinion, Lesson, Contact

admin.site.register(Opinion)


class CourseAdin(admin.ModelAdmin):
    list_display = ['title', 'teacher',  'price', 'language']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['number', 'title']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdin)