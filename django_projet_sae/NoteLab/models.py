# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Etudiant(models.Model):
    idetudiant = models.AutoField(db_column='idEtudiant', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    groupe = models.CharField(max_length=5)
    photo = models.TextField()
    email = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'Etudiant'

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.groupe}"

    def dico(self):
        return {"idprofesseur":self.idetudiant, "nom":self.nom, "prenom":self.prenom, "groupe":self.groupe, "photo":self.photo, "email":self.email,}


class Examen(models.Model):
    idexamen = models.AutoField(db_column='idExamen', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(max_length=45)
    date = models.DateField(blank=False, null=False)
    professeur_idprofesseur = models.ForeignKey('Professeur', models.CASCADE, db_column='Professeur_idProfesseur')  # Field name made lowercase.
    ressource_idressource = models.ForeignKey('Ressource', models.CASCADE, db_column='Ressource_idRessource')  # Field name made lowercase.
    coefficient = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Examen'

    def __str__(self):
        return f"{self.titre} par {self.professeur_idprofesseur}"

    def dico(self):
        return {"idexamen":self.idexamen, "titre":self.titre, "date":self.date, "professeur_idprofesseur":self.professeur_idprofesseur, "ressource_idressource":self.ressource_idressource, "coefficient": self.coefficient}


class Note(models.Model):
    idnote = models.AutoField(db_column='idNote', primary_key=True)  # Field name made lowercase.
    note = models.IntegerField()
    appreciation = models.TextField(blank=True, null=True)
    examen_idexamen = models.ForeignKey(Examen, models.CASCADE, db_column='Examen_idExamen')  # Field name made lowercase.
    etudiant_idetudiant = models.ForeignKey(Etudiant, models.CASCADE, db_column='Etudiant_idEtudiant')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Note'

    def dico(self):
        return {"idnote":self.idnote, "note":self.note, "appreciation":self.appreciation, "examen_idexamen":self.examen_idexamen, "etudiant_idetudiant":self.etudiant_idetudiant}

    def __str__(self):
        return f"{self.note}"


class Professeur(models.Model):
    idprofesseur = models.AutoField(db_column='idProfesseur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'Professeur'

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    def dico(self):
        return {"idprofesseur":self.idprofesseur, "nom":self.nom, "prenom":self.prenom}


class Ue(models.Model):
    idue = models.AutoField(db_column='idUE', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    semestre = models.IntegerField()
    creditects = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UE'

    def __str__(self):
        return f"{self.nom}"

    def dico(self):
        return {"idue":self.idue, "nom":self.nom, "semestre":self.semestre, "creditects":self.creditects}


class Ressource(models.Model):
    idressource = models.AutoField(db_column='idRessource', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    descriptif = models.TextField(blank=True, null=True)
    coefficient = models.IntegerField()
    ue_idue = models.ForeignKey(Ue, models.CASCADE, db_column='ue_idue')

    class Meta:
        managed = True
        db_table = 'Ressource'

    def __str__(self):
        return f"{self.nom}"

    def dico(self):
        return {"idressource":self.idressource, "nom":self.nom, "descriptif":self.descriptif, "coefficient":self.coefficient, "ue_idue":self.ue_idue}
