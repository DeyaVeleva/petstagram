from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
        null=False,
    )

    def save(self, *args, **kwargs) :
        super().save( *args, **kwargs)
        if not self.slug:
            self.slug=slugify(f'{self.name}-{self.id}')
        return super().save( *args, **kwargs)

    def __str__(self):
        return self.name