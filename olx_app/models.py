from django.db import models

from attribute.models import Attribute
from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    ads_count = models.IntegerField(default=0)


class SubCategory(BaseModel):
    title = models.CharField(max_length=100)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attributes = models.ManyToManyField('attribute.Attribute', blank=True)

    ads_count = models.IntegerField(default=0)


class Ads(BaseModel):
    title = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ads/', null=True, blank=True)
    content = models.TextField()

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    district = models.ForeignKey('comman.District', on_delete=models.CASCADE)

    is_top = models.BooleanField(default=False)


class AdsAtribute(BaseModel):
    value = models.CharField(max_length=100)

    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)


class AdsAtributeOptions(BaseModel):
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    ads_atribute_value = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    option = models.ForeignKey('attribute.AttributeOptions', on_delete=models.CASCADE)