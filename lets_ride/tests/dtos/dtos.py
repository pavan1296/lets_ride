from dataclasses import dataclass
import enum

@dataclass
class RideRequestDTO:
    from_place: str
    to_place: str
    is_flexible: bool
    flexible_from_time: str
    flexible_to_time: str
    no_of_seats: int
    luggage_quantity: int
    date_time: int


@dataclass
class AssetRequestDTO:
    from_place: str
    to_place: str
    is_flexible: bool
    flexible_from_time: str
    flexible_to_time: str
    date_time: int
    no_of_assets: int
    asset_type: str
    asset_sensitivity: enum
    whom_to_deliver: str