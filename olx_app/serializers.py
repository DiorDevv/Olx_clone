from rest_framework import serializers
from olx_app import models


class AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Ads
        fields = "__all__"
