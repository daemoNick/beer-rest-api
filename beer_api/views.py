from django.shortcuts import render
from rest_framework import viewsets
from beer_api import models
from beer_api import serializers


class BeerView(viewsets.ModelViewSet):
    queryset = models.BeerDiaryItem.objects.all()
    serializer_class = serializers.BeerSerializer
