from collections import Counter
from contextlib import contextmanager
from datetime import date,datetime
from time import time,sleep

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()
x = [1,2,3,4]

def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    try:
        start = time()
        yield
        end = time()
    
    except RuntimeError:
        pass
    
    finally:
        difference = end - start
        if difference >= OPERATION_THRESHOLD_IN_SECONDS:
            day = get_today()
            day = str(day.isocalendar()[2])
            violations.update(day)
            
        for k in violations:
            if violations[k] >= ALERT_THRESHOLD:
                print(ALERT_MSG)
        


for num in [0,2,0,3,4,5]:
    with timeit():
        sleep(num)