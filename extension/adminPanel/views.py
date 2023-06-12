from django.shortcuts import render, redirect
from login_register.models import Estudiante, Profesor, CursosDiplomados, Modalidad, ServicioDetalleEstado, Decano, Proyecto


# Create your views here.

def inProgressView(request):
    return render(request, 'inprogres.html')

def inProgressView1(request):
    return render(request, 'inprogres1.html')


def panelView(request):
    return render(request, 'panel.html')

def studentPanelView(request):
     return render(request, "studentPanel.html")

def coursesView(request):
    cursos = CursosDiplomados.objects.all()
    return render(request, 'cursos.html', {
        "cursos": cursos
    })

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

def servicesListView(request):
     servicios = ServicioDetalleEstado.objects.all()
     return render(request, 'servicios.html', {
          'servicios' : servicios
     })

def decanosListView(request):
     decanos = Decano.objects.all()
     return render(request, 'decano.html', {
          'decanos': decanos
     }) 

def projectsListView(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto.html', {
         'proyectos': proyectos
    })


def student_update(request):
    try:
        if request.method == 'POST':
            estudiante = Estudiante.objects.get(id=request.POST["id"])
            estudiante.nombre = request.POST["name"]
            estudiante.correo = request.POST["mail"]
            estudiante.rol = request.POST["role"]
            estudiante.save()
            return redirect("students")
        else:
            return render(request, 'update_student.html')
    except:
         error = "ID DONT MATCH"
         return render(request, 'update_student.html', {
              'error': error
         })
        

def update_courses(request):
    try:
        if request.method == 'POST':
            curso = CursosDiplomados.objects.get(id=request.POST["id"])
            curso.nombre = request.POST["nombre"]
            curso.id_profesor = Profesor.objects.get(id = request.POST["profesor"])
            curso.fecha = request.POST["fecha"]
            curso.id_modalidad = Modalidad.objects.get(id = request.POST["modalidad"])
            curso.save()
            return redirect("courses")
        else:
            return render(request, 'update_courses.html')
    except:
         error = "SOMETHING WRONG"
         return render(request, 'update_courses.html', {
              'error': error
         })
         

def add_courses(request):
    try:
        if request.method == 'POST':
                CursosDiplomados.objects.create(nombre = request.POST["nombre"], 
                id_profesor = Profesor.objects.get(id = request.POST["profesor"]), 
                fecha = request.POST["fecha"], 
                id_modalidad = Modalidad.objects.get(id = request.POST["modalidad"]))

                return redirect("courses")
        else:
            return render(request, 'add_courses.html')
    except:
        error = "SOMETHING WRONG"
        return render(request, 'add_courses.html', {
            'error': error
        })

    
    
def deleteCourse(request):
    if request.method == "POST":
        try:
                curso = CursosDiplomados.objects.filter(nombre = request.POST["nombre"]).first()
                curso.delete()
                return redirect("courses")
        except:
            error = "Course does not exits"
            return render(request, "deleteCourse.html", {'error': error})
    else:
            return render(request, "deleteCourse.html")


    
