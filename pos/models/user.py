from django.contrib.auth.models import User as DjangoUser

from django.db import models

from .stock import Order


class User(models.Model):
    card = models.CharField(max_length=255, unique=True)
    credit = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    crew = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField()
    is_cashier = models.BooleanField(default=False)

    @property
    def used(self):
        orders = Order.objects.filter(user_id=self.id)
        return sum([order.sum for order in orders])

    @property
    def left(self):
        return self.credit - self.used

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class UserSession(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    user = models.ForeignKey(User)
    django_user = models.ForeignKey(DjangoUser, blank=True)
