from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main'),
    path(
        'content/<category_slug>/<sub_category_slug>/<content_slug>/',
        views.content_detail_view,
        name='content_detail'
    ),
]
