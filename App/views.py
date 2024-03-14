from django.shortcuts import render
from App.models import  Estudiante, Curso, Profesor, Entregable
from App.forms import Estudiante_for, Curso_For, Profesor_for, Entregable_for
# Create your views here.

def inicio(request):
    return render(request,"App/inicio.html")

def curso(request):
    
    return render(request,"App/cursos.html")

def estudiante(request):
    
    return render(request,"App/estudiantes.html")


def profesor(request):
    
    return render(request,"App/profesores.html")


def entregables(request):
    
    return render(request,"App/entregables.html")

# FORMULARIOS ...................


def agregar_cursos(request):
    
    if request.method == "POST":
        
        formulario = Curso_For(request.POST)
        
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            
            nuevo_curso = Curso(nombre = info_dict["nombre"],
                                comision = info_dict["comision"]
                                )  
            nuevo_curso.save()
            
            return render(request, "App/inicio.html")
    else:
        formulario = Curso_For()
                
    return render(request, "App/nuevo_curso.html", {"form": formulario})


def agregar_estudiante(request):
    
    if request.method == "POST":
        
        formulario = Estudiante_for(request.POST)
        
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            
            nuevo_estudiante = Estudiante(nombre = info_dict["nombre"],
                                        apellido = info_dict["apellido"],
                                        email =  info_dict["email"],                               
                                        edad = info_dict["edad"]                                
                                        )  
            nuevo_estudiante.save()
            
            return render(request, "App/inicio.html")
    else:
        formulario = Estudiante_for()
                
    return render(request, "App/nuevo_estudiante.html", {"form": formulario})
    

def agregar_profesor(request):
    
    if request.method == "POST":
        
        formulario = Profesor_for(request.POST)
        
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            
            nuevo_profesor = Estudiante(nombre = info_dict["nombre"],
                                        apellido = info_dict["apellido"],
                                        email =  info_dict["email"],                               
                                        profesion = info_dict["profesion"]                                
                                        )  
            nuevo_profesor.save()
            
            return render(request, "App/inicio.html")
    else:
        formulario = Profesor_for()
                
    return render(request, "App/nuevo_profesor.html", {"form": formulario})
    


def agregar_entregas(request):
    
    if request.method == "POST":
        
        formulario = Entregable_for(request.POST)
        
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            
            nuevo_estudiante = Entregable(nombre = info_dict["nombre"],
                                        fechaEntrega = info_dict["fechaEntrega"],
                                        entregado =  info_dict["entregado"]                               
                                        )  
            nuevo_estudiante.save()
            
            return render(request, "App/inicio.html")
    else:
        formulario = Entregable_for()
                
    return render(request, "App/nuevo_entregable.html", {"form": formulario})
    
def buscar_profesor(request):
    
    return render(request, "App/buscar_profesor.html") 

def resultados_profesor(request):

    profesor = request.GET["nombre_profesor"] 
    
    resultados = Profesor.objects.filter(nombre_iexact=profesor)
    
    return render(request, "App/inicio.html",{"resultados":resultados})