# projeto/views.py
from django.shortcuts import render
from ..models import Projeto
from rest_framework import generics
from ..serializers import ProjetoSerializer
class ProjetoCreate(generics.CreateAPIView):
# API endpoint that allows creation of a new projeto
    queryset = Projeto.objects.all(),
    serializer_class = ProjetoSerializer
class ProjetoList(generics.ListAPIView):
# API endpoint that allows projeto to be viewed.
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
class ProjetoDetail(generics.RetrieveAPIView):
# API endpoint that returns a single projeto by pk.
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
class ProjetoUpdate(generics.RetrieveUpdateAPIView):
# API endpoint that allows a projeto record to be updated.
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
class ProjetoDelete(generics.RetrieveDestroyAPIView):
# API endpoint that allows a projeto record to be deleted.
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer