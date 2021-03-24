from django.shortcuts import render, HttpResponse
from .forms import FormContatto
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def contatti(request):
    if request.method == "POST":
        form = FormContatto(request.POST)
        if form.is_valid():
            print("Il form è valido!")
            print("NOME:", form.cleaned_data["nome"])
            print("COGNOME:", form.cleaned_data["cognome"])
            print("EMAIL:", form.cleaned_data["email"])
            print("CONTENUTO:", form.cleaned_data["contenuto"])
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("New post:", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
    else:
        form = FormContatto()

    context = {"form": form}
    return render(request, "contatto.html", context)
