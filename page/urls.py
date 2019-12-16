from django.conf.urls import url
from django.urls import path
from page.views import Home, Login, logout, signup, matricula, CursoContenido

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^cursos/(?P<id>\d+)/matricula/$', matricula, name='matricula'),
    path('curso_contenido/<int:id>', CursoContenido.as_view(), name='curso_contenido')
]