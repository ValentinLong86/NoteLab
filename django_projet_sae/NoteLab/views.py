import io
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.platypus import Table
from django.http import FileResponse

from django.shortcuts import render
from .models import Ue
from .forms import UeForm, ProfForm, RessourceForm, EtudiantForm, ExamenForm, NoteForm
from django.http import HttpResponseRedirect
from . import models



def index(request):
    return render(request, 'NoteLab/index.html')


def AjoutUE(request):
    if request.method == 'POST':
        form = UeForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/notelab/traitementue/")
        else:
            return render(request, 'NoteLab/ajoutue.html', {'form': form})
    else:
        form = UeForm()
        return render(request, 'NoteLab/ajoutue.html', {'form':form})


def TraitementUE(request):
    if request.method =="POST":
        pForm=UeForm(request.POST)
        if pForm.is_valid():
            equipementok = pForm.save()
            return render(request, 'NoteLab/traitementue.html', {'equipementok':equipementok})
        else:
            return render(request, 'NoteLab/ajoutue.html', {'form':pForm})


def DeleteUE(request, id):
    ue=models.Ue.objects.get(pk=id)
    ue.delete()
    return HttpResponseRedirect("/notelab/listeressourceue/")


def UpdateUE(request, id):
    updue=models.Ue.objects.get(pk=id)
    form = UeForm(updue.dico())
    return render(request, "NoteLab/ajoutue.html", {"form":form, "id":id})


def traitementUpdateUE(request, id):
    lform = UeForm(request.POST)
    if lform.is_valid():
        ueok=lform.save(commit=False)
        ueok.idue=id
        ueok.save()
        return HttpResponseRedirect("/notelab/listeressourceue/")
    else:
        return render(request, "NoteLab/ajoutue.html", {"form" : lform, "id": id})


def listeressourceue(request):
    liste = list(models.Ue.objects.all())
    listeres = list(models.Ressource.objects.all())
    return render(request, "NoteLab/listeressourceue.html",{"liste":liste, "listeres": listeres})


def AjoutRessource(request):
    if request.method == 'POST':
        form = RessourceForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/notelab/traitementressource/")
        else:
            return render(request, 'NoteLab/ajoutressource.html', {'form': form})
    else:
        form = RessourceForm()
        return render(request, 'NoteLab/ajoutressource.html', {'form':form})


def TraitementRessource(request):
    if request.method =="POST":
        pForm=RessourceForm(request.POST)
        if pForm.is_valid():
            ressouok = pForm.save()
            return render(request, 'NoteLab/traitementressource.html', {'ressouok':ressouok})
        else:
            return render(request, 'NoteLab/ajoutressource.html', {'form':pForm})


def DeleteRessource(request, id):
    res=models.Ressource.objects.get(pk=id)
    res.delete()
    return HttpResponseRedirect("/notelab/listeressourceue/")


def UpdateRessource(request, id):
    updres=models.Ressource.objects.get(pk=id)
    form = RessourceForm(updres.dico())
    return render(request, "NoteLab/ajoutressource.html", {"form":form, "id":id})


def traitementUpdateRessource(request, id):
    lform = RessourceForm(request.POST)
    if lform.is_valid():
        resok=lform.save(commit=False)
        resok.idressource=id
        resok.save()
        return HttpResponseRedirect("/notelab/listeressourceue/")
    else:
        return render(request, "NoteLab/ajoutressource.html", {"form" : lform, "id": id})


def AjoutProf(request):
    if request.method == 'POST':
        form = ProfForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/notelab/traitemenprof/")
        else:
            return render(request, 'NoteLab/ajoutprof.html', {'form': form})
    else:
        form = ProfForm()
        return render(request, 'NoteLab/ajoutprof.html', {'form':form})


def TraitementProf(request):
    if request.method =="POST":
        pForm=ProfForm(request.POST)
        if pForm.is_valid():
            profok = pForm.save()
            return render(request, 'NoteLab/traitementprof.html', {'profok':profok})
        else:
            return render(request, 'NoteLab/ajoutprof.html', {'form':pForm})


def DeleteProf(request, id):
    prof=models.Professeur.objects.get(pk=id)
    prof.delete()
    return HttpResponseRedirect("/notelab/listeprofexam/")


def UpdateProf(request, id):
    updprof=models.Professeur.objects.get(pk=id)
    form = ProfForm(updprof.dico())
    return render(request, "NoteLab/ajoutprof.html", {"form":form, "id":id})


def traitementUpdateProf(request, id):
    lform = ProfForm(request.POST)
    if lform.is_valid():
        profok=lform.save(commit=False)
        profok.idprofesseur=id
        profok.save()
        return HttpResponseRedirect("/notelab/listeprofexam/")
    else:
        return render(request, "NoteLab/ajoutprof.html", {"form" : lform, "id": id})


def listeprofexam(request):
    listeprof = models.Professeur.objects.all()
    listeexa= models.Examen.objects.all()
    return render(request, "NoteLab/listeprofexam.html",{"listeprof":listeprof, "listeexa":listeexa})


def AjoutEtudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/notelab/traitementetudiant/")
        else:
            return render(request, 'NoteLab/ajoutetudiant.html', {'form': form})
    else:
        form = EtudiantForm()
        return render(request, 'NoteLab/ajoutetudiant.html', {'form':form})


def TraitementEtudiant(request):
    if request.method =="POST":
        pForm=EtudiantForm(request.POST)
        if pForm.is_valid():
            etuok = pForm.save()
            return render(request, 'NoteLab/traitementetudiant.html', {'etuok':etuok})
        else:
            return render(request, 'NoteLab/ajoutetudiant.html', {'form':pForm})


def DeleteEtudiant(request, id):
    etu=models.Etudiant.objects.get(pk=id)
    etu.delete()
    return HttpResponseRedirect("/notelab/listeetudiant/")


def UpdateEtudiant(request, id):
    updetu=models.Etudiant.objects.get(pk=id)
    form = EtudiantForm(updetu.dico())
    return render(request, "NoteLab/ajoutetudiant.html", {"form":form, "id":id})


def traitementUpdateEtudiant(request, id):
    lform = EtudiantForm(request.POST)
    if lform.is_valid():
        etuok=lform.save(commit=False)
        etuok.idetudiant=id
        etuok.save()
        return HttpResponseRedirect("/notelab/listeetudiant/")
    else:
        return render(request, "NoteLab/ajoutetudiant.html", {"form" : lform, "id": id})


def listeetudiant(request):
    listenotes = models.Note.objects.all()
    listeetu = models.Etudiant.objects.all()
    return render(request, "NoteLab/listeetudiant.html",{"listeetu":listeetu, "listenotes":listenotes})


def AjoutExamen(request):
    if request.method == 'POST':
        form = ExamenForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/notelab/traitementexamen/")
        else:
            return render(request, 'NoteLab/ajoutexamen.html', {'form': form})
    else:
        form = ExamenForm()
        return render(request, 'NoteLab/ajoutexamen.html', {'form':form})


def TraitementExamen(request):
    if request.method =="POST":
        pForm=ExamenForm(request.POST)
        if pForm.is_valid():
            examok = pForm.save()
            return render(request, 'NoteLab/traitementexamen.html', {'examok':examok})
        else:
            return render(request, 'NoteLab/ajoutexamen.html', {'form':pForm})


def DeleteExamen(request, id):
    exam=models.Examen.objects.get(pk=id)
    exam.delete()
    return HttpResponseRedirect("/notelab/listeprofexam/")


def UpdateExamen(request, id):
    updexam=models.Examen.objects.get(pk=id)
    form = ExamenForm(updexam.dico())
    return render(request, "NoteLab/ajoutexamen.html", {"form":form, "id":id})


def traitementUpdateExamen(request, id):
    lform = ExamenForm(request.POST)
    if lform.is_valid():
        examok=lform.save(commit=False)
        examok.idexamen=id
        examok.save()
        return HttpResponseRedirect("/notelab/listeprofexam/")
    else:
        return render(request, "NoteLab/ajoutexamen.html", {"form" : lform, "id": id})


def AjoutNote(request):
    if request.method == 'POST':
        form = NoteForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/notelab/traitementnote/")
        else:
            return render(request, 'NoteLab/ajoutnote.html', {'form': form})
    else:
        form = NoteForm()
        return render(request, 'NoteLab/ajoutnote.html', {'form':form})


def TraitementNote(request):
    if request.method =="POST":
        pForm=NoteForm(request.POST)
        if pForm.is_valid():
            noteok = pForm.save()
            return render(request, 'NoteLab/traitementnote.html', {'noteok':noteok})
        else:
            return render(request, 'NoteLab/ajoutnote.html', {'form':pForm})


def DeleteNote(request, id):
    note=models.Note.objects.get(pk=id)
    note.delete()
    return HttpResponseRedirect("/notelab/listeetudiant/")


def UpdateNote(request, id):
    updnote=models.Note.objects.get(pk=id)
    form = NoteForm(updnote.dico())
    return render(request, "NoteLab/ajoutnote.html", {"form":form, "id":id})


def traitementUpdateNote(request, id):
    lform = NoteForm(request.POST)
    if lform.is_valid():
        noteok=lform.save(commit=False)
        noteok.idnote=id
        noteok.save()
        return HttpResponseRedirect("/notelab/listeetudiant/")
    else:
        return render(request, "NoteLab/listeetudiant.html", {"form" : lform, "id": id})


def generatePDF(request, id):
    etudiant = models.Etudiant.objects.get(idetudiant=id)
    notes = models.Note.objects.filter(etudiant_idetudiant = id)
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)
    p.drawString(cm, 28*cm, f"Notes de l'étudiant {etudiant}")
    data = [["Note", "Examen", "Appreciation"]]
    text = "/20"
    for n in notes:
        data.append([
            str(n.note) + text,
            n.examen_idexamen,
            n.appreciation,
        ])
    t = Table(data)
    t.wrapOn(p, 25 * cm, 100)
    t.drawOn(p, cm, 25 * cm)
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"Relevé de note de {etudiant.nom}.pdf")