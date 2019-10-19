from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
# Register your models here.
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date_of_attendance', 'student', 'status', 'remarks')
    list_filter = (('date_of_attendance',DateRangeFilter), 'student', 'status')
    date_hierarchy = 'date_of_attendance'

admin.site.register(Attendance, AttendanceAdmin)