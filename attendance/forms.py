from django import forms
import datetime
from .models import Attendance
from students.models import Students

class AttendanceForm(forms.ModelForm):
    date_of_attendance = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Attendance
        fields = ('date_of_attendance', 'student', 'status', 'remarks')

class AttendanceEveryStudentForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Students.objects.all())
    date_of_attendance = forms.DateField(widget=forms.SelectDateWidget(), initial=datetime.datetime.now())
    class Meta:
        model = Attendance
        fields = ('date_of_attendance', 'student', 'status', 'remarks')
    
    def __init__(self, *args, **kwargs):
        super(AttendanceEveryStudentForm, self).__init__( *args, **kwargs)

