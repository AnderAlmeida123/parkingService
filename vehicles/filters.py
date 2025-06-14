from dj_rql.filter_cls import AutoRQLFilterClass

from vehicles.models import VehicleType, Vehicle

class VehiclesTypeFilterClass(AutoRQLFilterClass):
    MODEL = VehicleType

class VehiclesFilterClass(AutoRQLFilterClass):
    MODEL = Vehicle