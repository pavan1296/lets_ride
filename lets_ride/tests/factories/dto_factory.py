import datetime
from factory import Factory
import factory
from lets_ride.tests.dtos.dtos import RideRequestDTO, AssetRequestDTO
from lets_ride.constants.enums import AssetSensitivity

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
    date_time = factory.LazyFunction(datetime.datetime.now)


class AssetRequestFactory(Factory):
    class Meta:
        model = AssetRequestDTO

    from_place = factory.Iterator(['Hyderabad', 'Bangaluru'])
    to_place = factory.Iterator(['Chennai', 'Mumbai'])
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    date_time = factory.LazyFunction(datetime.datetime.now)
    no_of_assets = factory.Sequence(lambda n: n + 1)
    asset_type = factory.Iterator(['Parcel', 'Documents'])
    asset_sensitivity = factory.LazyFunction(AssetSensitivity.get_list_of_values)
    whom_to_deliver = factory.Iterator(['pavan-7799888142'])