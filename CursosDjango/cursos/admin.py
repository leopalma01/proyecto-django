from django.contrib import admin
from .models import Cursos
from .models import Comentario
from .models import ComentarioContacto
from .models import ComentarioCurso

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('created' , 'updated')
    list_display = ('curso', 'duracion', 'carrera','horario','nombre')
    search_fields = ('curso', 'duracion', 'carrera','horario','nombre')
    date_hierarchy = 'created'
    list_filter = ('carrera','horario')

    def get_readonly_fields(self, request, obj=None):
#si el usuario pertenece al grupo de permisos "Usuario"
        if request.user.groups.filter(name="Usuarios").exists():
            return('curso','carrera','horario')
        else:
            return('created','updated')
    


admin.site.register(Cursos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

class AdministrarComentariosCurso(admin.ModelAdmin):
    list_display = ('id', 'carrera')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioCurso, AdministrarComentariosCurso)

