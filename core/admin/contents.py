from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline, TranslationStackedInline
from core.models.contents import TextContent, ImageContent, FileContent, StaffContent, PopupContent, Category, Content


# Category
# ----------------------------------------------------------------------------------------------------------------------
class ChildCategoryInline(admin.TabularInline):
    model = Category
    fk_name = 'parent'
    extra = 0
    fields = ('name', 'slug', 'category_type', 'order')
    show_change_link = True


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'category_type', 'parent', 'multiple', 'order', )
    list_filter = ('parent', 'category_type', 'multiple',)
    search_fields = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name_en', )}
    inlines = [ChildCategoryInline]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('parent')


# Content
# ----------------------------------------------------------------------------------------------------------------------
# TextContent
class TextContentTabular(TranslationTabularInline):
    model = TextContent
    extra = 0


# ImageContent
class ImageContentTabular(TranslationTabularInline):
    model = ImageContent
    extra = 0


# FileContent
class FileContentTabular(TranslationStackedInline):
    model = FileContent
    extra = 0


# StaffContent
class StaffContentTabular(TranslationStackedInline):
    model = StaffContent
    extra = 0


# PopupContent
class PopupContentInline(TranslationStackedInline):
    model = PopupContent
    extra = 0


# ContentAdmin
class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'category', 'order', )
    list_filter = ('category',)
    search_fields = ('title', 'slug', )
    prepopulated_fields = {'slug': ('title_en', )}
    inlines = [TextContentTabular, ImageContentTabular, FileContentTabular, StaffContentTabular, PopupContentInline, ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)