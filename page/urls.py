from django.conf.urls import url
from django.urls import path
from page.views import Home, Login, logout, signup, matricula, CursoContenido, AddCurso, Gestor, Teach

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^cursos/(?P<id>\d+)/matricula/$', matricula, name='matricula'),
    path('curso-contenido/<int:id>', CursoContenido.as_view(), name='curso_contenido'),
    path('agregar-curso', AddCurso.as_view(), name='add_curso'),
    path('gestor/', Gestor.as_view(), name='gestor_panel'),
    path('gestor/teach/<int:id>', Teach.as_view(), name='teach')
]