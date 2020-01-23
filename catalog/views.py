import json
from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
from .models import Dewey, Publication

# Create your views here.
CONTEXT_GLOBAL = {
    "mediatheque_name": "Bibliothèque de St Pons",
    "mediatheque_adr": "Villeneuve les Avignon",
    "dev_name": "Emmanuel Sandorfi",
    "dev_github": "https://github.com/pyfor19/babel-emmanuel",
    "dev_cadre": "Formation Django/Python FORMEXT",
}


def publication(request):

    try:
        # record = Dewey.objects.get(number="100")

        # record_list = Dewey.objects.all()
        record_list = Dewey.objects.filter(
            Q(number="000")
            | Q(number="100")
            | Q(number="200")
            | Q(number="300")
            | Q(number="400")
            | Q(number="500")
            | Q(number="600")
            | Q(number="700")
            | Q(number="800")
            | Q(number="900")
        )

        publication_list = Publication.objects.all()
    except:
        record_list = publication_list = None

    print(record_list.query)
    print(record_list)
    context_local = {
        "title": "Liste des publications du catalogue",
        "description": "Vous trouverez tous les ouvrages et leurs classifications",
    }
    context_page = {
        "global": CONTEXT_GLOBAL,
        "local": context_local,
        # "dewey_object": record,
        "dewey_object_list": record_list,
        "publication_object_list": publication_list,
    }
    return render(request, "catalog/publication.html", context=context_page)


def home(request):
    context_local = {
        "title": "Page d'accueil de Babel",
        "description": "Bienvenue sur cette page en cours de réalisation",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/index.html", context=context_page)


def about(request):
    context_local = {
        "title": "A propos de Babel",
        "description": "Vous trouverez tous les détails de spécifications ici.",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/about.html", context=context_page)


def newsroom(request):
    basedir = settings.BASE_DIR
    filename = basedir + "/scrap/checkurl.json"
    try:
        with open(filename, "r") as f:
            dict_checkurl = json.load(f)
    except Exception as e:
        dict_checkurl = {"error": str(e)}

    context_local = {
        "title": "Salle de Presse",
        "description": "Découvrez une liste de quotidiens internationaux",
    }

    # pour ajouter les deux dictionnaires onedict et anotherdict au dictionnaire bigdict,
    # j'utilise
    # bigdict = { **onedict, **anotherdict }

    context_page = {
        "checkurl": dict_checkurl,
        "local": context_local,
        "global": CONTEXT_GLOBAL,
    }

    return render(request, "catalog/newsroom.html", context=context_page)

