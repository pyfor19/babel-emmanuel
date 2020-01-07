from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=61, editable=False)
    century_birth = models.IntegerField(null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    place_birth = models.CharField(max_length=50, null=True, blank=True)

    date_died = models.DateField(null=True, blank=True)
    place_died = models.CharField(max_length=50, null=True, blank=True)

    content = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        if self.first_name:
            return f"{self.last_name}, {self.first_name}"
        else:
            return self.last_name

    # def save()


class Publication(models.Model):
    TYPE_PUBLICATION_CHOICES = [
        ("_", "Indéfini"),
        ("B", "Livres"),
        ("M", "Musique"),
        ("F", "Film"),
    ]

    name = models.CharField(max_length=61)
    reference = models.CharField(max_length=61, editable=False)
    type_publication = models.CharField(
        max_length=1, choices=TYPE_PUBLICATION_CHOICES, default="_",
    )
    genre = models.CharField(max_length=35)
    author = models.ForeignKey(Author, models.PROTECT, null=True)
    dewey_number = models.ForeignKey("Dewey", models.PROTECT, null=True)
    date_publication = models.DateField(null=True, blank=True)
    label_editor = models.CharField(max_length=50, null=True, blank=True)
    nb_tracks_pages = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

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
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=3)

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} - {self.name}"

