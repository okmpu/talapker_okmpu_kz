from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from core.models.main import Resource, Headliner


# ResourceAdmin
# ----------------------------------------------------------------------------------------------------------------------
class ResourceAdmin(TranslationAdmin):
    list_display = ('label', 'url', 'target', 'order', )


# HeadlinerAdmin
# ----------------------------------------------------------------------------------------------------------------------
class HeadlinerAdmin(TranslationAdmin):
    list_display = ('title', 'url', 'is_archive', 'order', )


admin.site.register(Resource, ResourceAdmin)
admin.site.register(Headliner, HeadlinerAdmin)
