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
