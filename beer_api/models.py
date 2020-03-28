from django.db import models

SERVINGTYPE = (
    (0, "Bottle"),
    (1, "Draft")
)

class BeerDiaryItem(models.Model):
    """Beer Diary Item """
    beer_name = models.CharField(max_length=50)
    brewer = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True, blank=True, default=0.0)
    serving_type = models.IntegerField(choices=SERVINGTYPE, default=0)
    description = models.CharField(max_length=255)

    def __str__(self):
        """Return the model as a string"""
        return self.beer_name
