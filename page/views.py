from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LoginForm, SignupForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login as django_login , logout as django_logout 
from .models import User, Curso
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        user = User.objects.filter(id=self.request.user.id).first()
        kwargs['user'] = user
        cursos = Curso.objects.all()
        kwargs['cursos'] = cursos
        kwargs['mis_cursos'] = cursos.filter(alumnos = user)
        
        return kwargs
        
class Login(TemplateView):
    template_name = 'login.html'
    
    def get_context_data(self, **kwargs):
        kwargs['login_form'] = LoginForm
        kwargs['signup_form'] = SignupForm
        user = User.objects.filter(id=self.request.user.id).first()
        kwargs['user'] = user
        return kwargs
        
    def post(self, request, *args, **kwargs):
        form = LoginForm(data = self.request.POST)
        if form.is_valid():
            print("es válido")
            email = self.request.POST['email']
            password = self.request.POST['password']
            print(email)
            print(password)
            username = User.objects.filter(email=email).first().username 
            print(username)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                django_login(self.request,user)
                return redirect('home')
            else:
                print('no existe este usuario')
                return render(self.request, "login.html", {'login_form': form, 'signup_form': SignupForm})
        else:
            print('form no válido')
            return render(self.request, "login.html",{'login_form': form, 'signup_form': SignupForm})


def logout(request):

    if request.method == 'POST':
        django_logout(request)
        print("L O G O U T")  
        return render(request, "home.html")
            
def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(data = request.POST)
        if form.is_valid():
            print("es válido")
            user = form.save()
            user.username = user.email.split('@')[0]
            user.save()
            django_login(request,user)
            return redirect('home')
        else:
            return render(request, "login.html", {'login_form': LoginForm, 'signup_form': form})
            

def matricula(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = User.objects.filter(id=request.user.id).first()
            print(curso)
            curso.alumnos.add(user)
            return redirect('home')
        else:
            return redirect('login')

class CursoContenido(TemplateView):
    template_name = 'curso_contenido.html'
    
    def get_context_data(self, **kwargs):
        id = kwargs.get('id')
        curso = Curso.objects.get(id=id)
        kwargs['curso'] = curso
        
        return kwargs
        