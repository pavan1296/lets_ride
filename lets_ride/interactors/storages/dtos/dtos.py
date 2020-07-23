from dataclasses import dataclass
from factory import Factory
import factory
import datetime

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