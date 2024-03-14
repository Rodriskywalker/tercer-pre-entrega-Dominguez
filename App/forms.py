from django import forms


class Estudiante_for(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField() 
    edad = forms.IntegerField()


class Curso_For(forms.Form):
    nombre = forms.CharField(max_length=30)
    comision = forms.IntegerField()


class Profesor_for(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)


class Entregable_for(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaEntrega = forms.DateField()
    entregado = forms.BooleanField()
