from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('results/', include('examresult.urls')),
    path('attendance/', include('attendance.urls')),
    path('students/', include('students.urls')),
    path('subjects/', include('subjects.urls')),
    path('admin/', admin.site.urls),
]