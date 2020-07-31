from dataclasses import dataclass
from factory import Factory
import factory
import datetime
from lets_ride.constants.enums import AssetSensitivity


@dataclass
class RideRequestDTO:
    from_place: str
    to_place: str
    is_flexible: bool
    flexible_from_time: str
    flexible_to_time: str
    no_of_seats: int
    luggage_quantity: int
    travel_date_time: str
    user_id: int


@dataclass
class AssetRequestDTO:
    from_place: str
    to_place: str
    travel_date_time: str
    is_flexible: bool
    flexible_from_time: str
    flexible_to_time: str
    no_of_assets: int
    asset_type: str
    asset_sensitivity: str
    whom_to_deliver: str
    user_id: int


@dataclass
class RideShareDTO:
    from_place: str
    to_place: str
    travel_date_time: str
    is_flexible: bool
    flexible_from_time: str
    flexible_to_time: str
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

class RideRequestDTOFactory(Factory):
    class Meta:
        model = RideRequestDTO

    from_place = factory.Iterator(['Hyderabad', 'Delhi', 'Mumbai'])
    to_place = factory.Iterator(['Chennai', 'Pune'])
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    no_of_seats = factory.Sequence(lambda n: n + 1)
    luggage_quantity = factory.Sequence(lambda n: n + 1)
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    user_id = factory.Sequence(lambda n: n + 1)


class AssetRequestDTOFactory(Factory):
    class Meta:
        model = AssetRequestDTO

    from_place = factory.Iterator(['Hyderabad', 'Delhi', 'Mumbai'])
    to_place = factory.Iterator(['Chennai', 'Pune'])
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    no_of_assets = 4
    asset_type = factory.Iterator(['Parcel', 'Documents'])
    asset_sensitivity = factory.LazyFunction(AssetSensitivity.get_list_of_values)
    whom_to_deliver = factory.Iterator(['Pavan-7799888142'])
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    user_id = 2


class RideShareDTOFactory(Factory):
    class Meta:
        model = RideShareDTO

    from_place = factory.Iterator(['Hyderabad', 'Delhi', 'Mumbai'])
    to_place = factory.Iterator(['Chennai', 'Pune'])
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    no_of_seats_available = factory.Sequence(lambda n: n + 1)
    assets_quantity = factory.Sequence(lambda n: n + 1)
    user_id = 2

