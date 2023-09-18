from django.db import models
from django.contrib.auth import get_user_model

# Create your models here

class StockSymbol(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    exchange = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol

class StockPrice(models.Model):
    symbol = models.ForeignKey(StockSymbol, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField()
    volume = models.PositiveIntegerField()

class UserStockWatchlist(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    stocks = models.ManyToManyField(StockSymbol)
    created_at = models.DateTimeField(auto_now_add=True)

class UserStockAlert(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    symbol = models.ForeignKey(StockSymbol, on_delete=models.CASCADE)
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_triggered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class UserPortfolio(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    stocks = models.ManyToManyField(StockSymbol)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class TradeHistory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    stock_symbol = models.ForeignKey(StockSymbol, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=[('buy', 'Buy'), ('sell', 'Sell')])
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
