from django.shortcuts import render  # noqa: F401
from django.http import HttpResponse
from .models import Produs, Question, Recenzie  # noqa: F401
from django.db.models import F  # noqa: F401

# Create your views here.
def salut(request):
    return render(request, "index.html")
    return HttpResponse("salut din Python")

def lista_produse(request):
    produse = Produs.objects.all().select_related("producator")
    if "pret_maxim" in request.GET:
        produse = produse.filter(pret__lte=int(request.GET["pret_maxim"]))
    if "search" in request.GET:
        produse = produse.filter(titlu__icontains=request.GET["search"])
    
    # produse = produse.order_by("pret") #pret crescator
    # produse = produse.order_by("-pret") #pret descrescator
    produse = produse.order_by("-pret", "-titlu") # pret desc in caz egalitate de pret filtreaza dupa titlu



    # for produs in produse:
    #     produs.pret += 1
    #     produs.save()
    # produse.update(pret=F("pret")+1)

    return render(request, "produse.html", {"produse": produse})



def produs(request, id):
    try:
        produs = Produs.objects.get(id=id)
        # recenzii = Recenzie.objects.filter(produs=produs)
        recenzii = produs.recenzie_set.all()
        recenzii_str = [recenzie.titlu for recenzie in recenzii]
    except Produs.DoesNotExist:
        return HttpResponse("Produsul nu exista")
    return HttpResponse(f"{produs}<br /> {recenzii_str}")


def quiz(request):
    question = Question.objects.first()
    text=question.text
    raspunsuri = [answer.value  for answer in question.answer_set.all()]
    return HttpResponse(f"{text} <br/> {raspunsuri}")