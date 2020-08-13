from enum import Enum

from ib_common.constants import BaseEnumClass


class RideRequestStatus(BaseEnumClass, Enum):
    confirm = "CONFIRM"
    pending = "PENDING"
    expired = "EXPIRED"


class AssetSensitivity(BaseEnumClass, Enum):
    highly_sensitive = "HIGHLY_SENSITIVE"
    sensitive = "SENSITIVE"
    normal = "NORMAL"

class ShareTravelStatus(BaseEnumClass, Enum):
    active = "ACTIVE"
    expired = "EXPIRED"


class TravelMedium(BaseEnumClass, Enum):
    bus = "BUS"
    car = "CAR"
    flight = "FLIGHT"
    ship = "SHIP"
    bike = "BIKE"
    train = "TRAIN"
    truck = "TRUCK"
    heavy_vehicle = "HEAVY_VEHICLE"
