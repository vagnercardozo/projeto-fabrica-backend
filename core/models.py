# core/models.py
from django.db import models

class Status(models.Model):
    descricao = models.CharField(max_length=1000)
    dt_criacao = models.DateField(auto_now_add=True, blank=True)
    def __str__(self):
        return f"{self.descricao}"

class Usuario(models.Model):
    nome = models.CharField(max_length=1000)
    tipo = models.CharField(max_length=1000)
    cpf = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    senha = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.nome}"
class Projeto(models.Model):
    titulo = models.CharField(max_length=1000)
    descricao = models.CharField(max_length=1000)
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    coordenador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.titulo}"

