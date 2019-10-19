from django.shortcuts import render
from .models import ExamResult
# Create your views here.

def index(request):
    results = ExamResult.objects.all()
    context = {
        'results' : results
    }
    return render(request, 'index.html', context)