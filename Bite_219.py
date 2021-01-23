from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    while True:
        for i in range(num_bites):
            new_date = start_date + timedelta(days=num_days)
            yield new_date
        start_date = new_date


gen = gen_bite_planning(1, 2, TODAY)
for i in range(10):
   print(next(gen))
