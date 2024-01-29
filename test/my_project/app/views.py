from django.shortcuts import render  # noqa: F401
from django.http import HttpResponse
from .models import Produs, Question, Recenzie  # noqa: F401
from django.db.models import F

# Create your views here.
def salut(request):
    return HttpResponse("salut")

def lista_produse(request):
    produse = Produs.objects.all()
    if "pret_maxim" in request.GET:
        produse = produse.filter(pret__lte=int(request.GET["pret_maxim"]))
    if "search" in request.GET:
        produse = produse.filter(titlu__icontains=request.GET["search"])
    
    # produse = produse.order_by("pret") #pret crescator
    # produse = produse.order_by("-pret") #pret descrescator
    produse = produse.order_by("-pret", "-titlu") # pret desc in caz egalitate de pret filtreaza dupa titlu

    produse_formatat = [
        f"<li>{produs.titlu} - {produs.pret} - {produs.stoc}</li>"
        for produs in produse
    ]

    # for produs in produse:
    #     produs.pret += 1
    #     produs.save()
    produse.update(pret=F("pret")+1)

    response_string = "<body><ul>"
    response_string += "".join(produse_formatat)
    response_string += "</ul></body>"
    return HttpResponse(response_string)


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