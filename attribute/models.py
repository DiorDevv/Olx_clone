from django.db import models

from utils.models import BaseModel


class Attribute(BaseModel):
    class AttributeTypes(models.TextChoices):
        # STRING = 'STRING'
        INTEGER = 'INTEGER'
        BUTTON = 'BUTTON'  # button select
        SELECT = 'SELECT'  # 2 lik tanlav
        MULTISELECT = 'MULTISELECT'  # ko'p tanlov

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='attribute/images/%Y/%m/%d', null=True, blank=True)
    type = models.CharField(max_length=255, choices=AttributeTypes.choices, default=AttributeTypes.INTEGER)
    is_required = models.BooleanField(default=False)
    is_listed = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        ordering = ('order',)


class AttributeOptions(BaseModel):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    attribute = models.ForeignKey(Attribute, related_name='options', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Attribute Options'
        verbose_name_plural = 'Attribute Options'
        ordering = ('order',)
