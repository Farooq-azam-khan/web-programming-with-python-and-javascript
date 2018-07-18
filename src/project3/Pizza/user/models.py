from django.db import models

from menu.models import (Topping,
                        PizzaOrder, 
                        SubsOrder,
                        PastaOrder,
                        SaladsOrder,
                        DinnerPlattersOrder)
                        
# Create your models here.
class User(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    pizza  = models.ForeignKey(PizzaOrder, on_delete=models.CASCADE, related_name='pizza')
    subs  = models.ForeignKey(SubsOrder, on_delete=models.CASCADE, related_name='subs')
    pasta = models.ForeignKey(PastaOrder, on_delete=models.CASCADE, related_name='pasta')
    salads = models.ForeignKey(SaladsOrder, on_delete=models.CASCADE, related_name='salads')
    dinner = models.ForeignKey(DinnerPlattersOrder, on_delete=models.CASCADE, related_name='dinner')
    
    def total_price(self):
        return 10.0
        
    def __str__(self):
        orders = [self.pizza, self.subs, self.pasta, self.salads, self.dinner]
        ret = f'{self.user} order: '
        for order in orders:
            if order:
                ret+= f'{order}'
        return ret