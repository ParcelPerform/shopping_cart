import uuid
from django.db import models


def order_code_generator():
    return str(uuid.uuid4()).split('-')[0].upper()


class Order(models.Model):
    PROCESSING = 'PR'
    DELIVERING = 'DE'
    FINISHED = 'FI'
    CANCELED = 'CA'
    STATUS_CHOICES = ((PROCESSING, 'Processing'),
                      (DELIVERING, 'Delivering'),
                      (FINISHED, 'Finished'),
                      (CANCELED, 'Canceled'),)
    order_code = models.CharField(max_length=10, default=order_code_generator)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PROCESSING)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)





class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.CharField(max_length=500)
    quantity = models.PositiveIntegerField(default=0)
