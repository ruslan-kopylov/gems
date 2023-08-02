from django.db import models


class Customer(models.Model):

    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    @property
    def spent_money(self):
        deals = Deal.objects.filter(customer=self)
        money = 0
        for deal in deals:
            money += deal.money
        return money


class Gem(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Deal(models.Model):

    date = models.DateTimeField()
    gem = models.ForeignKey(
        Gem, on_delete=models.CASCADE, related_name='deals',
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='deals',
    )
    money = models.IntegerField()
    quantity = models.IntegerField()
