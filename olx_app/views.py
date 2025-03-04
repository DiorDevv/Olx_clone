from django.shortcuts import render
from rest_framework import generics
from olx_app.serializers import AdsSerializers
from olx_app.models import Ads


class AdsListAPIView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers
