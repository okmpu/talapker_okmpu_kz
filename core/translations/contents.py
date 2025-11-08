from modeltranslation.translator import translator, TranslationOptions
from core.models.contents import Category, Content, TextContent, FileContent, StaffContent, ImageContent, \
    PopupContent


# Category
# ----------------------------------------------------------------------------------------------------------------------
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


# Content
# ----------------------------------------------------------------------------------------------------------------------
class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


# Contents
class TextContentTranslationOptions(TranslationOptions):
    fields = ('text', )


class ImageContentTranslationOptions(TranslationOptions):
    fields = ('image', )


class FileContentTranslationOptions(TranslationOptions):
    fields = ('caption', 'source_file', )


class StaffContentTranslationOptions(TranslationOptions):
    fields = ('full_name', 'activity', 'bio', )


class PopupContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Content, ContentTranslationOptions)
translator.register(TextContent, TextContentTranslationOptions)
translator.register(FileContent, FileContentTranslationOptions)
translator.register(ImageContent, ImageContentTranslationOptions)
translator.register(StaffContent, StaffContentTranslationOptions)
translator.register(PopupContent, PopupContentTranslationOptions)