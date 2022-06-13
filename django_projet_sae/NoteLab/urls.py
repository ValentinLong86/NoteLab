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

    path('ajoutressource/', views.AjoutRessource),
    path('traitementressource/', views.TraitementRessource),
    path('deleteressource/<int:id>/', views.DeleteRessource),
    path('updateressource/<int:id>/', views.UpdateRessource),
    path('updatetraitementressource/<int:id>/', views.traitementUpdateRessource),

    path('ajoutexamen/', views.AjoutExamen),
    path('traitementexamen/', views.TraitementExamen),
    path('deleteexamen/<int:id>/', views.DeleteExamen),
    path('updateexamen/<int:id>/', views.UpdateExamen),
    path('updatetraitementexamen/<int:id>/', views.traitementUpdateExamen),

    path('ajoutetudiant/', views.AjoutEtudiant),
    path('traitementetudiant/', views.TraitementEtudiant),
    path('deleteetudiant/<int:id>/', views.DeleteEtudiant),
    path('updateetudiant/<int:id>/', views.UpdateEtudiant),
    path('updatetraitementetudiant/<int:id>/', views.traitementUpdateEtudiant),
    path('listeetudiant/', views.listeetudiant),

    path('ajoutnote/', views.AjoutNote),
    path('traitementnote/', views.TraitementNote),
    path('deletenote/<int:id>/', views.DeleteNote),
    path('updatenote/<int:id>/', views.UpdateNote),
    path('updatetraitementnote/<int:id>/', views.traitementUpdateNote),
    path('listenote/', views.listenote),

    path('ajoutprof/', views.AjoutProf),
    path('traitementprof/', views.TraitementProf),
    path('listeprofexam/', views.listeprofexam),
    path('deleteprof/<int:id>/', views.DeleteProf),
    path('updateprof/<int:id>/', views.UpdateProf),
    path('updatetraitementprof/<int:id>/', views.traitementUpdateProf)
]
