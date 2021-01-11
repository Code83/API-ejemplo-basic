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
from django.db.models import Model, UUIdField, CharField, EmailField, DateTimeField
class Costumer(Model):
    id = UUIdField(primaryKey=True)
    name = CharField(max_lenght=45)
    surname = CharField(max_lenght=45)
    phone = CharField(max_lenght=45)
    email = EmailField()
