from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    is_teach = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.email)
    
class Curso(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 10, default='')
    alumnos = models.ManyToManyField(User, related_name='alumnos')
    profesor = models.ForeignKey(User, related_name='profesor', on_delete=models.CASCADE)
    
    def count_alumnos(self):
        num = self.alumnos.count()
        return num
        
    def __str__(self):
        return str(self.name)