from django import forms
from .models import Stock, UserStock


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['symbol', 'name', 'market_price']

class UserStockForm(forms.ModelForm):
    class Meta:
        model = UserStock
        fields = ['user', 'stock', 'quantity']