from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class PizzaOrder(models.Model):
    sicilian = models.BooleanField()
    large = models.BooleanField()
    toppings = models.ManyToManyField(Topping, blank=True, related_name="toppings")
    topping_number = models.IntegerField()
    
    def price(self):
        return 0.0
        
    def valid_topping_number(self):
        return self.topping_number > 0 and self.topping_number < 5
    def valid_toppings(self):
        return self.toppings.count() > self.topping_number or self.toppings.count() < self.topping_number

class SubsOrder(models.Model):
    name = models.CharField()
    large = models.BooleanField(blank=True)
    
    def price(self):
        return 0.0
        
    def __str__(self):
        return f''
    
    

class PastaOrder(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(blank=False, null=False)
    
    def __str__(self):
        return f'{self.name} {self.price}'

class SaladsOrder(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(blank=False, null=False)
    
    def __str__(self):
        return f'{self.name} {self.price}'

class DinnerPlattersOrder(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    large = models.BooleanField(blank=False)
    def price(self):
        return 0.0
        
    def __str__(self):
        return f'{self.name} {self.size}'
        