import json

import requests
from kafka import KafkaProducer
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Order, OrderLine


@api_view(['POST'])
def create_order(request):
    # tips: request body can be accessed using `request.data`
    # Store order to database
    # Call Warehouse API to send order to warehouse
    data = request.data

    order = Order()
    order.save()
    
    for line in data.get('items', []):
        item = line.get('name')
        quantity = line.get('quantity')
        ol = OrderLine(item=item, quantity=quantity, order=order)
        ol.save()

    # Challenge #2, linking one BE service to another
    requests.post('http://warehouse_api:5000/create-order/') 

    return Response(status=status.HTTP_200_OK,
                    data={"status": "success",
                          "data": request.data})
