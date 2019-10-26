from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='attendance'),
    path('add/', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('today/', views.render_all_students, name='today'),
    path('add_by_student/', views.add_by_student_today, name='test')
]