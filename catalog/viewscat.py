from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    FormView,
)
from django.utils.translation import gettext as _
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy
from django import forms
from .models import Publication, Dewey
from .views import CONTEXT_GLOBAL
from .utils import get_active_link, get_url

"""
productTitle
author a-link-normal
imgBlkFront
productDescriptionWrapper
detail_bullets_id content
"""


class MixinContextPage:
    title = _("Mon titre")
    description = _("Ma description")

    def get_mycontext(self):
        context_local = {
            "title": self.title,
            "description": self.description,
            get_active_link(self.request): "active",  # "publication",
        }
        context_page = {
            "global": CONTEXT_GLOBAL,
            "local": context_local,
        }
        return context_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_mycontext()
        return {**context, **context_page}


class PublicationByDewey(MixinContextPage, ListView):
    """
    Vue permettant de voir les publications filtrées par classement Dewey 
    """

    template_name = "catalog/publication-v2.html"
    context_object_name = "publication_object_list"
    # ajout du MixinContextPage pour hériter d'un context global et local
    # ajout du support de la traduction avec _()
    # title = _("Liste des Publications par Dewey")
    # rendre title dynamique et traduisible
    title = _("Dewey {}")
    description = _("Vous trouvez seulement les publications de cette catégorie")
    object_list = Publication.objects.all()

    def get_queryset(self):
        # argument dewey_number provenant de la structure de l'url
        self.deweynumber = self.kwargs["deweynumber"]

        # requête sur les publications avec le classement dewey spécifié dans l'url
        queryset = Publication.objects.filter(dewey_number__number=self.deweynumber)

        # et requête avec l'objet dewey
        self.currentdewey = Dewey.objects.get(number=self.deweynumber)
        self.publication_count = queryset.count()
        self.object_list = queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # requête pour avoir la liste du classement dewey
        context["dewey_object_list"] = Dewey.objects.filter(
            number__icontains="00"
        ) | Dewey.objects.filter(number__startswith=self.deweynumber[:1])

        # ajout de l'élément dewey actif
        context["dewey_active"] = self.currentdewey

        # diverses variables
        context["jumbotron_class"] = "dewey" + self.currentdewey.number
        context["publication_count"] = self.publication_count

        # appel de la fonction get_mycontext de MixinContextPage
        # traduction avec le deweynumber de l'url
        # self.title = _("Liste des Publications {}").format(self.kwargs["deweynumber"])
        # ou avec le display name de l'objet currentdewey récupéré dans get_queryset()
        self.title = self.title.format(self.currentdewey)
        context_page = self.get_mycontext()

        # retour de deux dictionnaires : context et context_page
        return {**context, **context_page}


class PublicationDetail(MixinContextPage, DetailView):
    template_name = "catalog/publication-detail-v2.html"
    model = Publication
    title = "Ma publication en détail"


class PublicationUpdate(MixinContextPage, UpdateView):
    template_name = "catalog/publication-update-v2.html"
    model = Publication
    title = "Je mets à jour la publication"
    fields = (
        "date_publication",
        "nb_tracks_pages",
        "content",
        "image_file",
        "image_url",
    )


"""
class PublicationByDewey(TemplateView):
    template_name = "catalog/publication.html"
"""
