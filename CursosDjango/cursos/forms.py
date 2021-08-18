from django import forms
from .models import ComentarioContacto
from .models import ComentarioCurso
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput, widgets


class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario','correo','mensaje']

class ComentarioFormCurso(forms.ModelForm):
    class Meta: 
        model = ComentarioCurso
        fields = ['mate','turno','carrera','instructor']

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox__label)s</label>%(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields =('titulo','descripcion','archivo')
        widgets={
            'archivo': CustomClearableFileInput
        }
       