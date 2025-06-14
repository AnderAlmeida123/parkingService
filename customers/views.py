from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser

from customers.filters import CustomerFilterClass
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    rql_filter_class = CustomerFilterClass
    # editar a permissao para quem pode fazer CRUD.
    permission_classes = [
        DjangoModelPermissions, IsAdminUser,
    ]
