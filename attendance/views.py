from django.shortcuts import render
from .models import Attendance
# Create your views here.

def index(request):
    attendance = Attendance.objects.all()
    context = {
        'attendance' : attendance
    }
    return render(request, 'attendance_sheet.html', context)