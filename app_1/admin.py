from django.contrib import admin
from .models import SClass, Schedule, Lesson, Time, Registration, Ways

class SheduleAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'lesson_id', 'time_id', 'week_day')
    list_display_links = ('class_id', 'lesson_id', 'time_id', 'week_day')
    search_fields = ('week_day',)

class SclassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class WaysAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'about', 'way', 'email', 'phone_number')
    list_display_links = ('first_name', 'last_name', 'age', 'about', 'way', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'age', 'about', 'way', 'email', 'phone_number')


admin.site.register(Schedule, SheduleAdmin)
admin.site.register(SClass, SclassAdmin)
admin.site.register(Lesson)
admin.site.register(Time)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Ways, WaysAdmin)