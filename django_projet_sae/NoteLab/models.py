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
    groupe = models.CharField(max_length=4)
    photo = models.TextField()
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Etudiant'

    def __str__(self):
        listeetu=f"{self.idetudiant} -|- Nom & Prenom de l'étudiant : {self.nom} {self.prenom}"
        return listeetu

    def dico(self):
        return {"idprofesseur":self.idetudiant, "nom":self.nom, "prenom":self.prenom, "groupe":self.groupe, "photo":self.photo, "email":self.email,}




class Examen(models.Model):
    idexamen = models.AutoField(db_column='idExamen', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(max_length=45)
    date = models.DateField(blank=False, null=False)
    professeur_idprofesseur = models.ForeignKey('Professeur', models.CASCADE, db_column='Professeur_idProfesseur')  # Field name made lowercase.
    ressource_idressource = models.ForeignKey('Ressource', models.CASCADE, db_column='Ressource_idRessource')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Examen'

    def __str__(self):
        listeexam=f"{self.idexamen} -|- Titre de l'examen : {self.titre} | Prof : {self.professeur_idprofesseur}, Ressource : {self.ressource_idressource}"
        return listeexam

    def dico(self):
        return {"idexamen":self.idexamen, "titre":self.titre, "date":self.date, "professeur_idprofesseur":self.professeur_idprofesseur, "ressource_idressource":self.ressource_idressource}




class Note(models.Model):
    idnote = models.AutoField(db_column='idNote', primary_key=True)  # Field name made lowercase.
    note = models.CharField(max_length=45)
    appreciation = models.TextField(blank=True, null=True)
    examen_idexamen = models.ForeignKey(Examen, models.CASCADE, db_column='Examen_idExamen')  # Field name made lowercase.
    etudiant_idetudiant = models.ForeignKey(Etudiant, models.CASCADE, db_column='Etudiant_idEtudiant')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Note'

    def dico(self):
        return {"idnote":self.idnote, "note":self.note, "appreciation":self.appreciation, "examen_idexamen":self.examen_idexamen, "etudiant_idetudiant":self.etudiant_idetudiant}

    def __str__(self):
        listenotes=f"{self.note}"
        return listenotes

class Professeur(models.Model):
    idprofesseur = models.AutoField(db_column='idProfesseur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Professeur'

    def __str__(self):
        listeprof=f"{self.idprofesseur} -|- Nom Prof : {self.nom}"
        return listeprof

    def dico(self):
        return {"idprofesseur":self.idprofesseur, "nom":self.nom, "prenom":self.prenom}

class Ue(models.Model):
    idue = models.AutoField(db_column='idUE', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    semestre = models.IntegerField()
    creditects = models.CharField(db_column='creditECTS', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UE'

    def __str__(self):
        liste=f"{self.idue} -|- UE : {self.nom}"
        return liste

    def dico(self):
        return {"idue":self.idue, "nom":self.nom, "semestre":self.semestre, "creditects":self.creditects}



class Ressource(models.Model):
    idressource = models.AutoField(db_column='idRessource', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45)
    descriptif = models.TextField(blank=True, null=True)
    #ue_idue = models.ForeignKey(Ue, models.CASCADE, db_column='idue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ressource'

    def __str__(self):
        listeres=f"{self.idressource} -|- Ressource : {self.nom}"
        return listeres

    def dico(self):
        return {"idressource":self.idressource, "nom":self.nom, "descriptif":self.descriptif, "ue_idue":self.ue_idue}








class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
