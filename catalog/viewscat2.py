import json
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django import forms
from django.urls import reverse_lazy
from .models import Publication, Dewey
from .views import CONTEXT_GLOBAL
from .viewscat import MixinContextPage


class PubContentForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = [
            "content",
            "image_file",
            "isbn",
            "date_publication",
            "dewey_number",
            "type_publication",
        ]


class PublicationUpdate(MixinContextPage, UpdateView):
    template_name = "catalog/publication-detail2.html"
    model = Publication
    title = "Ma publication mise à jour"

    fields = [
        "content",
        "image_file",
        "isbn",
        "date_publication",
        "dewey_number",
        "type_publication",
    ]

    def get_success_url(self, **kwargs):
        success_url = reverse_lazy(
            "publication-detail-pk", kwargs={"pk": self.object.pk}
        )
        return success_url
        # return self.object.get_absolute_url()


"""
class PublicationByDewey(TemplateView):
    template_name = "catalog/publication.html"
"""


def testajax(request):
    print("test request")
    if request.method == "POST":
        print(request.body)
        data = request.body
        return HttpResponse(json.dumps(data))
    else:
        data = "vide"
        return HttpResponse(json.dumps(data))
