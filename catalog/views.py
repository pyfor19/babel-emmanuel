import json
from django.shortcuts import render
from django.conf import settings

# Create your views here.
CONTEXT_GLOBAL = {
    "mediatheque_name": "Bibliothèque de St Pons",
    "mediatheque_adr": "Villeneuve les Avignon",
    "dev_name": "Emmanuel Sandorfi",
    "dev_github": "https://github.com/pyfor19/babel-emmanuel",
    "dev_cadre": "Formation Django/Python FORMEXT",
}


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

    dict_context = {
        "jumbotron_title": "Bienvenue sur notre page Babel",
        "jumbotron_p": "Vous aurez toutes les informations plus tard...",
        "checkurl": dict_checkurl,
    }

    return render(request, "catalog/newsroom.html", context=dict_context)

