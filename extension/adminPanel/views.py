from django.shortcuts import render
from login_register.models import Estudiante, Profesor


# Create your views here.


def panelView(request):
    return render(request, 'panel.html')

def studentsListView(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {
        'estudiantes': estudiantes
    })

def teacherListView(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {
        'profesores': profesores
    })

def student_update(request):
    return render(request, 'update_student.html')

def add_courses(request):
    return render(request, 'add_courses.html')

def update_courses(request):
    return render(request, 'update_courses.html')