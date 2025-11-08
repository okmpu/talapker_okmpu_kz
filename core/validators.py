from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_file_size(value):
    file_size = value.size
    max_size_mb = 10
    if file_size > max_size_mb * 1024 * 1024:
        raise ValidationError(_(f"Maximum file size: {max_size_mb}MB"))


def validate_image(image):
    max_size = 1 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError(_('The image size should not exceed 1MB.'))

    try:
        img = Image.open(image)
        width, height = img.size
        max_resolution = 1080

        if width != height:
            raise ValidationError(_('The image should be square'))

        if width > max_resolution or height > max_resolution:
            raise ValidationError(_('The maximum image resolution is 1024x1024px'))

    except Exception as e:
        raise ValidationError(
            _('The image could not be processed. Make sure that the file is a valid image'))


def validate_poster(image):
    max_size = 2 * 1024 * 1024  # 2MB
    if image.size > max_size:
        raise ValidationError(_('The image size should not exceed 2MB'))

    try:
        img = Image.open(image)
        width, height = img.size
        min_width, min_height = 640, 320

        if width < min_width or height < min_height:
            raise ValidationError(_('Minimum image resolution: 640x320px'))

        if width <= height:
            raise ValidationError(_('The image should be in landscape orientation (width is greater than height)'))

    except Exception:
        raise ValidationError(
            _('The image could not be processed. Make sure that the file is a valid image'))
