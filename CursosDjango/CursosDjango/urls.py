"""CursosDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from Contenido import views
from django.conf import settings
from cursos import views as views_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_cursos.registros, name="Registros"),
    
    path('contacto/',views_cursos.formulario,name="Contacto"),
    path('curso/',views.curso, name="Curso"),
    path('contacto/',views.contactos,name="ContactoOri"),
    path('example/',views.example,name="Example"),
    path('registrar/',views_cursos.registrar,name="Registrar"),
    path('consultarComentario/',views_cursos.consultarComentarioContacto,name="Comentarios"),
    path('eliminarComentario/<int:id>/', views_cursos.eliminarComentarioContacto, name='Eliminar'),
    path('formEditarComentario/<int:id>/', views_cursos.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_cursos.editarComentarioContacto, name='Editar'),
    path('consultas1',views_cursos.consultar1,name="Consultas"),
    path('consultas2',views_cursos.consultar2,name="Consultas2"),
    path('consultas3',views_cursos.consultar3,name="Consultas3"),
    path('consultas4',views_cursos.consultar4,name="Consulta4"),
    path('consultas5',views_cursos.consultar5,name="Consulta5"),
    path('formularioCurso/',views_cursos.formularioCurso, name="Cursos"),
    path('registrarCurso/',views_cursos.registrarCurso, name="RegistrarCurso"),
    path('consultarComentarioCurso/',views_cursos.consultarComentarioCurso, name="Comentarios2"),
    path('eliminarCurso/<int:id>/',views_cursos.eliminarCurso, name='EliminarCurso'),
     path('editarCurso/<int:id>/',views_cursos.consultarComentarioIndividualCurso, name='Curso'),
    path('comentarioCurso/<int:id>/',views_cursos.editarComentarioCurso, name="EditarCurso"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
