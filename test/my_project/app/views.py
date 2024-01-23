from django.shortcuts import render
from django.http import HttpResponse
from .models import Produs, Question

# Create your views here.
def salut(request):
    return HttpResponse("salut")

def lista_produse(request):
    produse = Produs.objects.all()
    if "pret_maxim" in request.GET:
        produse = produse.filter(pret__lte=int(request.GET["pret_maxim"]))
    if "search" in request.GET:
        produse = produse.filter(titlu__icontains=request.GET["search"])
    

    produse_formatat = [
        f"<li>{produs.titlu} - {produs.pret} - {produs.stoc}</li>"
        for produs in produse
    ]
    response_string = "<ol>"
    response_string += "".join(produse_formatat)
    response_string+= "</ol>"
    return HttpResponse(response_string)




def quiz(request):
    question = Question.objects.first()
    text=question.text
    raspunsuri = [answer.value  for answer in question.answer_set.all()]
    return HttpResponse(f"{text} <br/> {raspunsuri}")