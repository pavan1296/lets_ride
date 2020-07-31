import datetime
from factory import Factory
import factory
from lets_ride.tests.dtos.dtos import RideRequestDTO, AssetRequestDTO, RideShareDTO, ShareTravelInfoDTO
from lets_ride.constants.enums import AssetSensitivity, TravelMedium

class RideRequestDTOFactory(Factory):
    class Meta:
        model = RideRequestDTO

    from_place = factory.Iterator(['Hyderabad', 'Bangaluru'])
    to_place = factory.Iterator(['Chennai', 'Mumbai'])
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    no_of_seats = factory.Sequence(lambda n: n + 1)
    luggage_quantity = factory.Sequence(lambda n: n + 1)
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    user_id = 2

class AssetRequestFactory(Factory):
    class Meta:
        model = AssetRequestDTO

    from_place = factory.Iterator(['Hyderabad', 'Bangaluru'])
    to_place = factory.Iterator(['Chennai', 'Mumbai'])
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    no_of_assets = factory.Sequence(lambda n: n + 1)
    asset_type = factory.Iterator(['Parcel', 'Documents'])
    asset_sensitivity = factory.LazyFunction(AssetSensitivity.get_list_of_values)
    whom_to_deliver = factory.Iterator(['pavan-7799888142'])
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


class ShareTravelInfoFactory(Factory):
    class Meta:
        model = ShareTravelInfoDTO

    from_place = factory.Iterator(['Hyderabad', 'Delhi', 'Mumbai'])
    to_place = factory.Iterator(['Chennai', 'Pune'])
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    travel_medium = factory.LazyFunction(TravelMedium.get_list_of_values)
    assets_quantity = factory.Sequence(lambda n: n + 1)
    user_id = 2