from django.contrib import admin
from django.utils.translation import gettext as _

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Author, Publication, Dewey, DeweyTest


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class PublicationResource(resources.ModelResource):
    class Meta:
        model = Publication


class DeweyResource(resources.ModelResource):
    class Meta:
        model = Dewey


class PublicationAdmin(ImportExportModelAdmin):
    resource_class = PublicationResource
    list_display = (
        "name",
        "reference",
        "type_publication",
        "isbn",
        "author",
        "dewey_number",
        "date_publication",
        "label_editor",
    )

    fields_reference = ("type_publication", "dewey_number", ("isbn", "reference"))
    fields_publication = ("name", "author", "label_editor")
    fields_detail = (
        "date_publication",
        "nb_tracks_pages",
        "content",
        "image_file",
        "image_url",
    )

    fieldsets = (
        (_("Référence"), {"fields": fields_reference}),
        (_("Publication"), {"fields": fields_publication}),
        (_("Détail"), {"fields": fields_detail, "classes": ("collapse",)}),
    )
    readonly_fields = ("reference",)
    radio_fields = {"type_publication": admin.HORIZONTAL}
    autocomplete_fields = ["dewey_number", "author"]
    search_fields = ["name"]
    list_filter = ("dewey_number__number", "author__last_name")


class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
    list_display = (
        "last_name",
        "first_name",
        "date_birth",
        "century_birth",
    )
    fields_identity = (
        ("first_name", "last_name"),
        ("date_birth", "century_birth"),
        "place_birth",
    )
    fields_death = (("date_died", "place_died"),)
    fields_detail = (
        "content",
        "image_file",
        "image_url",
    )

    fieldsets = (
        (_("Identité"), {"fields": fields_identity}),
        (_("Détail"), {"fields": fields_detail, "classes": ("collapse",)}),
        (_("Contemporain ?"), {"fields": fields_death, "classes": ("collapse",)}),
    )
    readonly_fields = ("century_birth",)
    search_fields = (
        "last_name",
        "first_name",
        "age",
    )
    list_filter = ("century_birth",)


class DeweyAdmin(ImportExportModelAdmin):
    resource_class = DeweyResource
    list_display = (
        "number",
        "name",
    )
    search_fields = (
        "number",
        "name",
    )


class DeweyTestAdmin(DeweyAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)
admin.site.register(DeweyTest, DeweyTestAdmin)
