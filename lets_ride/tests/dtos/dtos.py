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
    travel_date_time: int
    user_id: int

@dataclass
class AssetRequestDTO:
    from_place: str
    to_place: str
    is_flexible: bool
    flexible_from_time: str
    flexible_to_time: str
    travel_date_time: int
    no_of_assets: int
    asset_type: str
    asset_sensitivity: enum
    whom_to_deliver: str
    user_id: int

@dataclass
class RideShareDTO:
    from_place: str
    to_place: str
    is_flexible: bool
    flexible_from_time: str
    flexible_to_time: str
    travel_date_time: str
    no_of_seats_available: int
    assets_quantity: int
    user_id: int


@dataclass
class ShareTravelInfoDTO:
    from_place: str
    to_place: str
    is_flexible: bool
    flexible_from_time: str
    flexible_to_time: str
    travel_date_time: str
    travel_medium: str
    assets_quantity: int
    user_id: int