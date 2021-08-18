
from django.shortcuts import render
from .models import Cursos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from .forms import ComentarioFormCurso
from .models import ComentarioCurso
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def registros(request):
    cursos=Cursos.objects.all()
    return render(request, "cursos/principal.html", {'cursos':cursos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():#si los datos recibidos son correctos
            form.save()#inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request,"cursos/consultaContacto.html",
                    {'comentarios':comentarios})
    form = ComentarioContactoForm()
    return render(request, 'cursos/contacto.html',{'form':form})

def formulario(request):
    return render(request, "cursos/contacto.html")

def consultarComentarioContacto(request):
        comentarios=ComentarioContacto.objects.all()
        #all recupera todos los objetos del modelo (registros de la tabla 
        #comentariosContacto)

        return render(request,"cursos/consultaContacto.html",
                                            {'comentarios':comentarios})
        #Indicamos el lugar donde se renderizará el resultado de esta vista
        # y enviamos la lista de comentarios recuparados.

def eliminarComentarioContacto(request, id, 
        confirmacion='cursos/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        if request.method == 'POST':
            comentario.delete()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"cursos/consultaContacto.html",
                    {'comentarios':comentarios})
        return render(request,confirmacion,{'object':comentario})

def consultarComentarioIndividual(request, id):
        comentario=ComentarioContacto.objects.get(id=id)

        return render(request,"cursos/formEditarComentario.html",
                {'comentario':comentario})

def editarComentarioContacto(request, id):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            comentarios=ComentarioContacto.objects.all()
            return render(request, "cursos/consultaContacto.html",
                    {'comentarios':comentarios})
        return render(request, "cursos/formEditarComentario.html",
                {'comentario':comentario})

def consultar1(request):
#con una sola condición
        cursos=Cursos.objects.filter(carrera="TIC")
        return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar2(request):
#multiples condiciones adicionando .filter() se analiza 
#como AND
        cursos=Cursos.objects.filter(carrera="TIC").filter(horario="Matutino")
        return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar3(request):
#Si solo deseamos recuperar ciertos datos agregamos la 
#función only, listando los campos que queremos obtener de 
#la consulta emplear filter() o #en el ejemplo all()
        cursos=Cursos.objects.all().only("curso", "duracion", "carrera", "horario", "nombre")
        return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar4(request):
        cursos=Cursos.objects.filter(horario__contains="Vesp")
        return render(request,"cursos/consultas.html",{'cursos':cursos})

def consultar5(request):
        cursos=Cursos.objects.filter(nombre__in=["Juan", "Luis"])
        return render(request,"cursos/consultas.html",{'cursos':cursos})

#cursos
def formularioCurso(request):
    return render(request,"cursos/curso.html")

def registrarCurso(request):
    if request.method == 'POST':
        form = ComentarioFormCurso(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios=ComentarioCurso.objects.all()
            return render(request,"cursos/consultaCurso.html",{'comentarios':comentarios})
    form = ComentarioFormCurso()
    return render(request,'cursos/curso.html',{'form': form})

def consultarComentarioCurso(request):
    comentarios=ComentarioCurso.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla
    #comentariosContacto)
    return render(request,"cursos/consultaCurso.html",{'comentarios':comentarios})

def eliminarCurso(request, id,
        confirmacion='cursos/eliminarCurso.html'):
        comentario = get_object_or_404(ComentarioCurso, id=id)
        if request.method=='POST':
            comentario.delete()
            comentarios=ComentarioCurso.objects.all()
            return render(request,"cursos/consultaCurso.html",
                {'comentarios':comentarios})
        return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividualCurso(request, id):
        comentario=ComentarioCurso.objects.get(id=id)
        return render(request,"cursos/editarCurso.html",
                {'comentario':comentario})

def editarComentarioCurso(request, id):
        comentario = get_object_or_404(ComentarioCurso, id=id)
        form = ComentarioFormCurso(request.POST, instance=comentario)

        if form.is_valid():
            form.save() #si el registro ya existe, se modifica.
            comentarios=ComentarioCurso.objects.all()
            return render(request,"cursos/consultaCurso.html",
                    {'comentarios':comentarios})

        return render(request,"cursos/editarCurso.html",
                {'comentario':comentario})
  

#archivos
def archivos(request):
        if request.method == 'POST':
                form = FormArchivos(request.POST, request.FILES)
                if form.is_valid():
                        titulo = request.POST['titulo']
                        descripcion = request.POST['descripcion']
                        archivo = request.FILES['archivo']
                        insert = Archivos(titulo=titulo, descripcion=descripcion, 
                        archivo=archivo)
                        insert.save()
                        return render(request,"cursos/archivos.html")
                else:
                        messages.error(request, "Error al procesar el formulario")
        else:
                return render(request,"cursos/archivos.html",{'archivo':Archivos})

def consultasSQL(request):
        cursos=Cursos.objects.raw('SELECT id,
        curso, duracion, carrera, horario, nombre, imagen FROM 
        cursos_cursos WHERE carrera="TIC" ORDER BY 
        horario DESC')
        return render(request,"cursos/consultas.html",
        {'cursos':cursos})