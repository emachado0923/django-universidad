from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarcurso', views.registrarcurso),
    path('edicioncurso/<codigo>', views.edicioncurso),
    path('eliminarcurso/<codigo>', views.eliminarcurso),
    path('editarcurso', views.editarcurso)
]
