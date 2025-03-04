from rest_framework import serializers
from attribute import models


class AttributeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Attribute
        fields = "__all__"
