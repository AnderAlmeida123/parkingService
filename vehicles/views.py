from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser

from core.permissions import IsOwnerOfVehicleOrRecord
from vehicles.filters import VehiclesTypeFilterClass, VehiclesFilterClass
from vehicles.models import Vehicle, VehicleType
from vehicles.serializer import VehicleSerializer, VehicleTypeSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    rql_filter_class = VehiclesTypeFilterClass

    permission_classes = [
        DjangoModelPermissions, IsAdminUser

    ]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    rql_filter_class = VehiclesFilterClass

    permission_classes = [
        DjangoModelPermissions, IsOwnerOfVehicleOrRecord
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
