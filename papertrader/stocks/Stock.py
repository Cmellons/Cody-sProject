from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Add this line to store current price
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol