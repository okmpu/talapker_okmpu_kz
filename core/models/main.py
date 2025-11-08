from django.db import models
from django.utils.translation import gettext_lazy as _
from core.validators import validate_poster


# Resource
# ----------------------------------------------------------------------------------------------------------------------
class Resource(models.Model):
    label = models.CharField(_('Label'), max_length=128)
    url = models.URLField(_('URL'))
    target = models.BooleanField(_('Target'), default=False)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')
        ordering = ('order', )


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
class Headliner(models.Model):
    title = models.CharField(_('Title'), max_length=64)
    poster = models.ImageField(
        _('Poster'), upload_to='register/public/headliners/',
        blank=True, null=True, validators=[validate_poster]
    )
    about = models.TextField(_('About'), blank=True, null=True)
    url = models.CharField(_('URL'), max_length=128, default='/')
    is_archive = models.BooleanField(_('Is archive'), default=False)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Headliner')
        verbose_name_plural = _('Headliners')
        ordering = ('order', )
