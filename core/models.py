
# core/models.py
from django.db import models

class Status(models.Model):
    descricao = models.CharField(max_length=1000)
    dt_criacao = models.DateField(auto_now_add=True, blank=True)

class Projeto(models.Model):
    titulo = models.CharField(max_length=1000)
    descricao = models.CharField(max_length=1000)
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    def __str__(self):
        return f"Projeto for {self.titulo}"