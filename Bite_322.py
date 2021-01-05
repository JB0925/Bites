from datetime import datetime, date
from freezegun import freeze_time


@freeze_time('2021-07-09')
def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    today = date.today()

    if not day_of_year:
        start = date(2021,1,1)
        day_of_year = int(str(today - start).split()[0])

    reading_progress = books_read / books_goal
    elapsed_time = day_of_year / 365
    return reading_progress >= elapsed_time
    



print(ontrack_reading(60,34))