from django.db import models


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    coingecko_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name
