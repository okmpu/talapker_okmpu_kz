from modeltranslation.translator import translator, TranslationOptions
from core.models.main import Resource, Headliner


# Resource
# ----------------------------------------------------------------------------------------------------------------------
class ResourceTranslationOptions(TranslationOptions):
    fields = ('label', )


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
class HeadlineTranslationOptions(TranslationOptions):
    fields = ('title', 'about', )


translator.register(Resource, ResourceTranslationOptions)
translator.register(Headliner, HeadlineTranslationOptions)
