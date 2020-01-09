from django.contrib import admin
from .models import Author, Publication, Dewey


class PublicationAdmin(admin.ModelAdmin):
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
        ("Reference", {"fields": fields_reference}),
        ("Publication", {"fields": fields_publication}),
        ("Detail", {"fields": fields_detail, "classes": ("collapse",)}),
    )
    readonly_fields = ("reference",)
    radio_fields = {"type_publication": admin.HORIZONTAL}
    autocomplete_fields = ["dewey_number", "author"]
    search_fields = ["name"]


class AuthorAdmin(admin.ModelAdmin):
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
        ("Identity", {"fields": fields_identity}),
        ("Detail", {"fields": fields_detail, "classes": ("collapse",)}),
        ("Died", {"fields": fields_death, "classes": ("collapse",)}),
    )
    readonly_fields = ("century_birth",)
    search_fields = ["last_name", "first_name"]


class DeweyAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "name",
    )
    search_fields = ["number", "name"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)
