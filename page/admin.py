from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    
class UserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'email', 'username', 'is_staff','is_superuser','last_login']

admin.site.register(User, UserAdmin)
admin.site.register(Curso, CursoAdmin)