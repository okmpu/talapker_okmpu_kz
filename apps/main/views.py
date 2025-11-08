from django.shortcuts import render, get_object_or_404

from core.models.contents import Category, Content
from core.models.main import Headliner


# Main page
# ----------------------------------------------------------------------------------------------------------------------
def main_view(request):
    headliners = Headliner.objects.filter(is_archive=False)
    context = {
        'headliners': headliners,
    }
    return render(request, 'app/page.html', context)


# Content detail page
# ----------------------------------------------------------------------------------------------------------------------
# content detail page
def content_detail_view(request, category_slug, sub_category_slug, content_slug):
    category = get_object_or_404(Category, slug=category_slug)
    sub_category = get_object_or_404(Category, parent=category, slug=sub_category_slug)
    content = get_object_or_404(Content.objects.select_related('category'), category=sub_category, slug=content_slug)

    contents = (
        Content.objects
        .filter(category__parent=category)
        .select_related('category')
    )

    context = {
        'content': content,
        'category': category,
        'sub_category': sub_category,

        'contents': contents,
        'open_sub_ids': { sub_category.id },
    }
    return render(request, 'app/content/page.html', context)
