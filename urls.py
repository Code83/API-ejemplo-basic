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

from rest_framework.routers import DefaultRouter
from customer.views import CustomerViewSet
router = DefaultRouter()
router.register('customers', CustomerViewSet, 'Customer')
urlpatterns = router.urls