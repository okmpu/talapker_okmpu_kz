from core.models.contents import Category
from core.models.main import Resource


def global_context(request):
    categories = Category.objects.filter(parent__isnull=True).order_by('order').prefetch_related('children')
    resources = Resource.objects.all().order_by('order')

    return {
        'categories': categories,
        'resources': resources
    }


