from django.shortcuts import render
from .models import Ue
from .forms import UeForm, ProfForm
from django.http import HttpResponseRedirect
from . import models
# Create your views here.


def index(request):
    return render(request, 'NoteLab/index.html')



def AjoutUE(request):
    if request.method == 'POST':
        form = UeForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/noteLab/traitementue/")
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
    return HttpResponseRedirect("/noteLab/listeressourceue/")



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
        return HttpResponseRedirect("/noteLab/listeressourceue/")
    else:
        return render(request, "NoteLab/ajoutue.html", {"form" : lform, "id": id})

def listeressourceue(request):
    liste = list(models.Ue.objects.all())
    return render(request, "NoteLab/listeressourceue.html",{"liste":liste})







def AjoutProf(request):
    if request.method == 'POST':
        form = ProfForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/noteLab/traitemenprof/")
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
    return HttpResponseRedirect("/noteLab/listeprofexam/")



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
        return HttpResponseRedirect("/noteLab/listeprofexam/")
    else:
        return render(request, "NoteLab/ajoutprof.html", {"form" : lform, "id": id})


def listeprofexam(request):
    listeprof = list(models.Professeur.objects.all())
    return render(request, "NoteLab/listeprofexam.html",{"listeprof":listeprof})

