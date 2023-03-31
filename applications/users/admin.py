from django.contrib import admin

from .models import User

class UsersAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'username',
        'nombres',
        'apellidos',
        'ocupation',
        'proyecto',
        'genero',
        'email',
    )
    search_fields = ('nombres',)
    list_filter = ('proyecto',)
    

admin.site.register(User, UsersAdmin)
