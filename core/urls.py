# projeto/urls.py
from django.urls import include, path
from .views import ProjetoCreate, ProjetoList, ProjetoDetail, ProjetoUpdate, ProjetoDelete
urlpatterns = [
    path('create/', ProjetoCreate.as_view(), name='create-projeto'),
    path('', ProjetoList.as_view()),
    path('<int:pk>/', ProjetoDetail.as_view(), name='retrieve-projeto'),
    path('update/<int:pk>/', ProjetoUpdate.as_view(), name='update-projeto'),
    path('delete/<int:pk>/', ProjetoDelete.as_view(), name='delete-projeto'),
]