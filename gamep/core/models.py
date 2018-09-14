from django.db import models
# Create your models here.


class Pessoa(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=64)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True, blank=True)


class Aluno(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True, blank=True)
