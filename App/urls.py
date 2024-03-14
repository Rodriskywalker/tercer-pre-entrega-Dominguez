from django.urls import path
from App.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("cursos/", curso, name="Cursos"),
    path("profesores/", profesor, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("entregables/", entregables, name="Entregables"),
    path("nuevo_profesor/", agregar_profesor,),
    path("nuevo_estudiante/", agregar_estudiante),
    path("nuevo_entregable/", agregar_entregas),
    path("nuevo_curso/", agregar_cursos),
    
    path("buscar_profesor/", buscar_profesor),
    path("resultados/", resultados_profesor),
]
