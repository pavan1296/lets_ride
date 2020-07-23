import datetime
import factory
from lets_ride.constants.enums import RideRequestStatus
from lets_ride.models.ride_request import RideRequest


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