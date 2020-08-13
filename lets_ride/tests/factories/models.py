import datetime
import factory
from lets_ride.constants.enums import RideRequestStatus, TravelMedium
from lets_ride.models.ride_request import RideRequest
from lets_ride.models.ride_share import RideShare
from lets_ride.models.share_travel_info import ShareTravelInfo


class RideRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RideRequest

    from_place = factory.Iterator(['Hyderabad', 'Delhi', 'Mumbai'])
    to_place = factory.Iterator(['Chennai', 'Pune'])
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    no_of_seats = factory.Sequence(lambda n: n + 1)
    luggage_quantity = factory.Sequence(lambda n: n + 1)
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    status = factory.LazyFunction(RideRequestStatus.get_list_of_values)
    user_id = 2


class RideShareFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RideShare

    from_place = factory.Iterator(['Hyderabad', 'Delhi', 'Mumbai'])
    to_place = factory.Iterator(['Chennai', 'Pune'])
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    no_of_seats_available = factory.Sequence(lambda n: n + 1)
    assets_quantity = factory.Sequence(lambda n: n + 1)
    status = factory.LazyFunction(RideRequestStatus.get_list_of_values)
    user_id = 2
    ride_requests = factory.Sequence(lambda n: n + 1)


class ShareTravelInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShareTravelInfo

    from_place = factory.Iterator(['Hyderabad', 'Delhi', 'Mumbai'])
    to_place = factory.Iterator(['Chennai', 'Pune'])
    travel_date_time = factory.LazyFunction(datetime.datetime.now)
    is_flexible = True
    flexible_from_time = factory.LazyFunction(datetime.datetime.now)
    flexible_to_time = factory.LazyFunction(datetime.datetime.now)
    travel_medium = factory.LazyFunction(TravelMedium.get_list_of_values)
    assets_quantity = factory.Sequence(lambda n: n + 1)