from django.contrib import admin

# Register your models here.
from .models import ExamResult

class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'marks')
    list_filter = ('student', 'subject')

admin.site.register(ExamResult, ExamResultAdmin)