from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Estudiante

# Create your views here.

def loginView(request):
    if request.method == "POST": 
        try:
            usuario = Estudiante.objects.get(correo = request.POST["mail"])

            if usuario.contraseña == request.POST["contraseña"] and request.POST["rol"] == "ADMIN":
                return redirect("admin")
            
            elif usuario.contraseña == request.POST["contraseña"] and (request.POST["rol"] == "STUDENT" or request.POST["rol"] == "Student"):
                return redirect("student")
            
            else:
                error = "Password dont match"
                return render(request, "login.html", {"error": error})
                 
        except:
            error = "User does not exists"
            return render(request, "login.html", {"error": error})
      
    return render(request, "login.html")

def registerView(request):
    if request.method == "POST":
        if request.POST["contraseña"] == request.POST["confirmPassword"]:
                    try:
                        Estudiante.objects.create(nombre = request.POST["userName"],
                        correo = request.POST["mail"],
                        contraseña = request.POST["contraseña"],
                        rol = request.POST["rol"]
                        )
                        print(Estudiante.objects.get(correo = request.POST["mail"]))
                        if request.POST["rol"] == "ADMIN":
                            return redirect("admin")
                        else:
                             return redirect("student")
                    except:
                        error = 'User already exists'
                        return render(request, "register.html", {'error': error})
                         
        else:
            error = 'Password dont match'
            return render(request, "register.html", {'error': error})
    return render(request, "register.html")

       

            
