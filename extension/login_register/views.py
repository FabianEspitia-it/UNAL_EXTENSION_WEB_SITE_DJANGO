from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Estudiante

# Create your views here.

def loginView(request):
    if request.method == "POST":
        try:
            Estudiante.objects.get(correo = request.POST["mail"])
            return redirect("admin")
        except:
            error = "User does not exists"
            return render(request, "login.html", {"error": error})

    return render(request, "login.html")

def registerView(request):
    if request.method == "POST":
        if request.POST["contraseña"] == request.POST["confirmPassword"]:
                    try:
                        print(Estudiante.objects.get(correo = request.POST["mail"]))
                        Estudiante.objects.create(nombre = request.POST["userName"],
                        correo = request.POST["mail"],
                        contraseña = request.POST["contraseña"],
                        rol = request.POST["rol"]
                        )
                        return redirect("admin")
                    except:
                        error = 'User already exists'
                        return render(request, "register.html", {'error': error})
                         
        else:
            error = 'Password dont match'
            return render(request, "register.html", {'error': error})
    return render(request, "register.html")

       

            
