from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('C:/Users/superuser/Bites')
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    bite_number = []
    fastest_time = 5

    with open(timings_log) as f:
        reader = f.readlines()
        for row in reader:
            row = row.replace('=', '').split()
            if 'no' not in row:
                bite, tests_passed, time = int(row[0]), int(row[1]), float(row[-2])
                current_bite_time = time / tests_passed
                if current_bite_time < fastest_time:
                    fastest_time = current_bite_time
                    bite_number.clear()
                    bite_number.append(str(bite))
                if current_bite_time == fastest_time:
                    bite_number.append(str(bite))
    
    bite_number = list(set(bite_number))

    if len(bite_number) > 1:
        return min(bite_number), max(bite_number)
    return bite_number[0]
                
    


print(get_bite_with_fastest_avg_test([]))