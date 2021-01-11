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
from rest_framework import serializers
from customer.models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer