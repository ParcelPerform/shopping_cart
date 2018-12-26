from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Order, OrderLine


@api_view(['POST'])
def create_order(request):
    # TODO: Store order to database
    # Call Warehouse API to send order to warehouse
    return Response(status=status.HTTP_200_OK, data={"status": "success", "data": {}})

