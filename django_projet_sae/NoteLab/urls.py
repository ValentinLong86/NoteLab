from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('ajoutue/', views.AjoutUE),
    path('traitementue/', views.TraitementUE),
    path('listeressourceue/', views.listeressourceue),
    path('deleteue/<int:id>/', views.DeleteUE),
    path('updateue/<int:id>/', views.UpdateUE),
    path('updatetraitementue/<int:id>/', views.traitementUpdateUE),
    path('ajoutprof/', views.AjoutProf),
    path('traitementprof/', views.TraitementProf),
    path('listeprofexam/', views.listeprofexam),
    path('deleteprof/<int:id>/', views.DeleteProf),
    path('updateprof/<int:id>/', views.UpdateProf),
    path('updatetraitementprof/<int:id>/', views.traitementUpdateProf)
]
