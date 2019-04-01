from django.db import models



# from django.contrib.auth.models import User

class State(models.Model):
    energy = models.IntegerField()
    filth = models.IntegerField()
    day_light = models.IntegerField()
    milk = models.IntegerField()
    milk_val = models.IntegerField()
    eggs = models.IntegerField()
    eggs_val = models.IntegerField()
    bacon = models.IntegerField()
    bacon_val = models.IntegerField()
    money = models.IntegerField()
    wallet = models.IntegerField()
    cow_price = models.IntegerField()
    cow_count = models.IntegerField()
    pig_price = models.IntegerField()
    pig_count = models.IntegerField()
    coop_price = models.IntegerField()
    coop_count = models.IntegerField()
    timestamp           = models.DateTimeField(auto_now_add=True)
