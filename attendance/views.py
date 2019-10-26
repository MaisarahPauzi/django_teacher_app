from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from .forms import AttendanceForm, AttendanceEveryStudentForm
import datetime
from students.models import Students
from django.views.generic import CreateView


def index(request):
    attendance = Attendance.objects.all()
    context = {
        'attendance' : attendance
    }
    return render(request, 'attendance_sheet.html', context)

def add(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/attendance')
    else:
        form = AttendanceForm()
    return render(request, 'attendence_form.html', {'form': form})

def update(request, id):
    attendance = get_object_or_404(Attendance, id=id)
    if request.method == "POST":
        form = AttendanceForm(request.POST,  instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('/attendance')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendence_update.html', {'attendance':attendance,'form': form})

def delete(request, id):
    attendance = get_object_or_404(Attendance, id=id)
    attendance.delete()
    return redirect('/attendance')

def today(request, id):
    student_id = id
    if request.method == "POST":
        form = AttendanceEveryStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/attendance')
    else:
        form = AttendanceEveryStudentForm()

    return render(request, 'attendance_bulk.html', context)


def render_all_students(request):
    students = Students.objects.all()
    date_today = datetime.datetime.now()

    context = {
        'students' : students,
        'date': date_today        
    }
    return render(request, 'attendance_student_list.html', context)

def add_by_student_today(request):
    student_id = request.GET.get('id')
    student = Students.objects.get(id=student_id)
    date_today = datetime.datetime.now()
    status = request.GET.get('status')
    remarks = request.GET.get('remarks')
    context = {
        'id': student_id,
        'date': date_today,
        'status': status,
        'remarks': remarks
    }
    if status:
        new_attendance = Attendance(student=student, date_of_attendance=date_today,status=True, remarks=remarks)
    else:
        new_attendance = Attendance(student=student, date_of_attendance=date_today,status=False, remarks=remarks)
    new_attendance.save()

    return redirect('/attendance/today')


    