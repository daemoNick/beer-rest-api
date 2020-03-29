from rest_framework import serializers
from beer_api import models

class BeerSerializer(serializers.ModelSerializer):
    """Serializes Beer Diary item"""

    class Meta:
        model = models.BeerDiaryItem
        fields = ('id', 'beer_name', 'brewer', 'created_on', 'price', 'serving_type', 'description')
