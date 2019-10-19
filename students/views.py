from django.shortcuts import render
from .models import Students
# Create your views here.

def index(request):
    students = Students.objects.all()
    context = {
        'students' : students
    }
    return render(request, 'student_list.html', context)