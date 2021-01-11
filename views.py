#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gaguajardo
#
# Created:     08-01-2021
# Copyright:   (c) gaguajardo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from rest_framework import viewsets
from customer.models import Customer
from customer.serializers import CustomerSerializer
class CustomerViewSet (viewsets.ModelViewSet):
    model = Customer
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
