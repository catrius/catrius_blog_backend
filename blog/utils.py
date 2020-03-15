from django.utils.text import slugify


def unique_slugify(Model, field):
    slug = slugify(field)
    duplicate_slug_count = Model.objects.filter(slug__iregex=fr'^{slug}-?\d*$').count()
    return slug if duplicate_slug_count == 0 else f'{slug}-{duplicate_slug_count + 1}'
