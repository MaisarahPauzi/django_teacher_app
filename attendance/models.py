from django.db import models
from students.models import Students

# Create your models here.
class Attendance(models.Model):
    date_of_attendance = models.DateField(auto_now=False)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    status = models.BooleanField()
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.date_of_attendance}'