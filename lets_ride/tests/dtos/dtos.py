from dataclasses import dataclass
import factory
from factory import Factory
import datetime
import string
import factory.fuzzy


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