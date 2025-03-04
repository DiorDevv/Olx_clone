from django.urls import path, include
from .views import AdsListAPIView

urlpatterns = [
    path('', AdsListAPIView.as_view(), name='ads_list'),
]
