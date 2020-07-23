from enum import Enum

from ib_common.constants import BaseEnumClass


class RideRequestStatus(BaseEnumClass, Enum):
    confirm = "CONFIRM"
    pending = "PENDING"
    expired = "EXPIRED"
