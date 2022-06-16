from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class ProfForm(ModelForm):
    class Meta:
        model = models.Professeur
        fields = ("idprofesseur", "nom", "prenom")
        labels = {
            "idprofesseur": _("ID"),
            "nom": _("Nom"),
            "prenom": _("Prénom"),
        }


class UeForm(ModelForm):
    class Meta:
        model = models.Ue
        fields = ("idue", "nom", "semestre", "creditects")
        labels = {
            "idue": _("ID"),
            "nom": _("Nom"),
            "semestre": _("Semestre"),
            "creditects": _("Créditects"),
        }


class RessourceForm(ModelForm):
    class Meta:
        model = models.Ressource
        fields = ("idressource", "nom", "descriptif", "coefficient", "ue_idue")
        labels = {
            "idressource": _("ID"),
            "nom": _("Nom"),
            "descriptif": _("Descriptif"),
            "ue_idue": _("UE"),
            "coefficient": _("Coefficient"),
        }


class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ("idetudiant", "nom", "prenom", "groupe", "photo", "email")
        labels = {
            "idetudiant": _("ID"),
            "nom": _("Nom"),
            "prenom": _("Prenom"),
            "groupe": _("Groupe"),
            "photo": _("Photo"),
            "email": _("Email"),
        }


class ExamenForm(ModelForm):
    class Meta:
        model = models.Examen
        fields = ("idexamen", "titre", "date", "professeur_idprofesseur", "ressource_idressource", "coefficient")
        labels = {
            "idexamen": _("ID"),
            "titre": _("Titre"),
            "date": _("Date"),
            "professeur_idprofesseur": _("Professeur"),
            "ressource_idressource": _("Ressource"),
            "coefficient": _("Coefficient"),
        }


class NoteForm(ModelForm):
    class Meta:
        model = models.Note
        fields = ("idnote", "note", "appreciation", "examen_idexamen", "etudiant_idetudiant")
        labels = {
            "idnote": _("ID"),
            "note": _("Note"),
            "appreciation": _("Appréciation"),
            "examen_idexamen": _("Examen"),
            "etudiant_idetudiant": _("Etudiant"),
        }



