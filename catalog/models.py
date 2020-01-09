from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext as _
from .utils import get_century

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("Prénom")
    )
    last_name = models.CharField(max_length=30, verbose_name=_("Nom"))
    name = models.CharField(max_length=61, editable=False)
    century_birth = models.IntegerField(null=True, blank=True, verbose_name=_("Siècle"))
    date_birth = models.DateField(
        null=True, blank=True, verbose_name=_("Date de naissance")
    )
    place_birth = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Lieu de naissance")
    )

    date_died = models.DateField(null=True, blank=True, verbose_name=_("Date de décès"))
    place_died = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Lieu de décès")
    )

    content = models.TextField(null=True, blank=True, verbose_name=_("Contenu"))
    image_url = models.URLField(
        null=True, blank=True, verbose_name=_("URL d'une image")
    )
    image_file = models.ImageField(
        null=True, blank=True, verbose_name=_("Fichier image")
    )

    class Meta:
        ordering = ["last_name"]
        verbose_name = _("Auteur")

    def __str__(self):
        if self.first_name:
            return f"{self.last_name}, {self.first_name}"
        else:
            return self.last_name

    def clean(self):
        """
        1) update of century from <date_birth> using catalog.utils.get_century function
        2) update name in <first_name space last_name> or <last_name>
        """
        if self.date_birth:
            century = get_century(self.date_birth.year)
            self.century_birth = century
        if self.first_name:
            self.name = f"{self.first_name} {self.last_name}"
        else:
            self.name = self.last_name


class Publication(models.Model):
    TYPE_PUBLICATION_CHOICES = [
        ("B", "Livres"),
        ("M", "Musique"),
        ("F", "Film"),
        ("*", "Autre"),
    ]

    name = models.CharField(max_length=61, verbose_name=_("Prénom"))
    reference = models.CharField(
        max_length=61, editable=False, verbose_name=_("Référence")
    )
    type_publication = models.CharField(
        max_length=1,
        choices=TYPE_PUBLICATION_CHOICES,
        default="B",
        verbose_name=_("Type de publication"),
    )
    # genre = models.CharField(max_length=35)
    author = models.ForeignKey(
        Author, models.PROTECT, null=True, verbose_name=_("Auteur")
    )
    dewey_number = models.ForeignKey(
        "Dewey", models.PROTECT, null=True, verbose_name=_("Classement DEWEY")
    )
    date_publication = models.DateField(
        null=True, blank=True, verbose_name=_("Date de publication")
    )
    label_editor = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Editeur/Label")
    )
    nb_tracks_pages = models.IntegerField(
        null=True, blank=True, verbose_name=_("Nb de pages/morceaux")
    )
    content = models.TextField(null=True, blank=True, verbose_name=_("Contenu"))
    image_url = models.URLField(null=True, blank=True, verbose_name=_("URL d'image"))
    image_file = models.ImageField(
        null=True, blank=True, verbose_name=_("Fichier image")
    )
    isbn = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("ISBN")
    )

    class Meta:
        ordering = ["reference"]

    def __str__(self):
        return f"{self.reference} {self.name}"

    def clean(self):
        if self.dewey_number and self.author:
            self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = ""


class Dewey(models.Model):
    class Meta:
        ordering = ["number"]

    name = models.CharField(max_length=150, verbose_name=_("Libellé"))
    number = models.CharField(max_length=12, verbose_name=_("Numéro"))
    bg_color = models.CharField(max_length=7, default="*", editable=False)
    text_color = models.CharField(max_length=7, default="*", editable=False)

    DEWEY_COLOR_CHOICES = [
        # format dewey family, bg color, text color
        ("000", "#000000", "#fff"),  # Black
        ("100", "#8B4513", "#fff"),  # Marroon
        ("200", "#FF0000", "#fff"),  # Red
        ("300", "#FF4500", "#fff"),  # Orange
        ("400", "#FFFF00", "#000"),  # Yellow
        ("500", "#32CD32", "#fff"),  # Green
        ("600", "#1E90FF", "#fff"),  # Blue
        ("700", "#8B008B", "#fff"),  # Purple
        ("800", "#A9A9A9", "#fff"),  # Grey
        ("900", "#FFFFFF", "#000"),  # White
    ]

    def colored_number(self):
        if self.number:
            try:
                i = int(self.number[:1])
                return format_html(
                    '<span style=" background-color: {}; color: {}; display: inline-block; padding: .3rem; min-width: 50px;">{}</span>',
                    self.DEWEY_COLOR_CHOICES[i][1],  # bg color
                    self.DEWEY_COLOR_CHOICES[i][2],  # text color
                    self.number,
                )
            except:
                return "Wrong format"

    def __str__(self):
        return f"{self.number} - {self.name}"
        # return self.colored_number()
