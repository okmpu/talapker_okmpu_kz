from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline, TranslationStackedInline
from django.utils.translation import gettext_lazy as _
from core.admin.mixins import LinkedAdminMixin
from core.models.contents import TextContent, ImageContent, FileContent, StaffContent, PopupContent, Category, Content


# Category
# ----------------------------------------------------------------------------------------------------------------------
# ChildCategoryInline
class ChildCategoryInline(LinkedAdminMixin, TranslationStackedInline):
    model = Category
    fk_name = 'parent'
    prepopulated_fields = {'slug': ('name_en', )}
    extra = 0
    readonly_fields = ('detail_link',)

    def detail_link(self, obj):
        return self.admin_link(obj, 'category', label=_('Detail view'))

    detail_link.short_description = _('Detail link')


# ContentInline
class ContentInline(LinkedAdminMixin, TranslationStackedInline):
    model = Content
    extra = 0
    fields =  ('title_kk', 'title_ru', 'title_en', 'slug', 'order', 'detail_link', )
    readonly_fields = ('detail_link', )

    def detail_link(self, obj):
        return self.admin_link(obj, 'content', label=_('Detail view'))
    detail_link.short_description = _('Detail link')

    def has_module_permission(self, request):
        return True

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('category')


# CategoryAdmin
class CategoryAdmin(LinkedAdminMixin, TranslationAdmin):
    list_display = ('name', 'slug', 'category_type', 'parent', 'multiple', 'order', )
    list_filter = ('parent', 'category_type', 'multiple',)
    search_fields = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name_en', )}
    readonly_fields = ('parent_detail_link',)
    inlines = []

    def get_inline_instances(self, request, obj=None):
        inlines = []

        if obj is not None:
            if obj.category_type == 'content':
                inlines.append(ContentInline(self.model, self.admin_site))

            inlines.append(ChildCategoryInline(self.model, self.admin_site))

        return inlines

    def parent_detail_link(self, obj):
        return self.parent_link(obj, 'parent')

    parent_detail_link.short_description = _('Parent category')



# Content
# ----------------------------------------------------------------------------------------------------------------------
# TextContent
class TextContentTabular(TranslationStackedInline):
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
class ContentAdmin(LinkedAdminMixin, TranslationAdmin):
    list_display = ('title', 'slug', 'category', 'order', )
    list_filter = ('category',)
    search_fields = ('title', 'slug', )
    prepopulated_fields = {'slug': ('title_en', )}
    readonly_fields = ('parent_detail_link', )
    inlines = (TextContentTabular, ImageContentTabular, FileContentTabular, StaffContentTabular, PopupContentInline, )

    def parent_detail_link(self, obj):
        return self.parent_link(obj, 'category')

    parent_detail_link.short_description = _('Category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)