from datetime import date
from typing import Dict, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    decisions = {}

    for item in renting_history:
        month = f'{item.date.year}-{item.date.month}'
        if month not in decisions:
            decisions[month] = item.price
        else:
            decisions[month] += item.price
    
    for month in decisions:
        if decisions[month] > STREAMING_COST_PER_MONTH:
            decisions[month] = STREAM
        else:
            decisions[month] = RENT
    
    return decisions


m = [MovieRented('Spider-Man', 12, date(2020, 12, 28)),
     MovieRented('Sonic', 10, date(2020, 11, 4)),
     MovieRented('Die Hard', 3, date(2020, 11, 3))]
print(rent_or_stream(m))