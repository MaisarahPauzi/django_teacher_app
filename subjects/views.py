from django.shortcuts import render
from .models import Subjects
# Create your views here.

def index(request):
    subjects = Subjects.objects.all()
    context = {
        'subjects' : subjects
    }
    return render(request, 'subject_list.html', context)