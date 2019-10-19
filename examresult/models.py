from django.db import models
from students.models import Students
from subjects.models import Subjects
# Create your models here.

class ExamResult(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'{self.student}'
