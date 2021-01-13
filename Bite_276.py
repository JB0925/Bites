from pathlib import Path
from urllib.request import urlretrieve

from dateutil.parser import parse

# get the data
tmp = Path('C:/Users/superuser/Bites')
base_url = 'https://bites-data.s3.us-east-2.amazonaws.com/'

fathers_days_countries = tmp / 'fathers-day-countries.txt'
fathers_days_recurring = tmp / 'fathers-day-recurring.txt'

for file_ in (fathers_days_countries, fathers_days_recurring):
    if not file_.exists():
        urlretrieve(base_url + file_.name, file_)


def _parse_father_days_per_country(year, filename=fathers_days_countries):
    """Helper to parse fathers_days_countries"""
    countries = []
    dates = []

    with open(filename) as f:
        reader = f.readlines()
        for row in reader:
            if '* ' in row:
                names = row.split('* ')[1].replace('\n','').replace('and ', '')
                countries.append(names.split(', '))
                
            if str(year) in row:
                dates.append(row.split(': ')[1].replace('\n',''))
        
    return dict(zip(dates, countries))

    
def _parse_recurring_father_days(filename=fathers_days_recurring):
    """Helper to parse fathers_days_recurring"""
    recurring_dates = {}
    dates = []
    countries = []

    with open(filename) as f:
        reader = f.readlines()
        for row in reader[1:]:
            if '* ' in row:
                dates.append(row.split('* ')[1].replace('\n',''))
            
            if row != '\n' and '* ' not in row:
                countries.append(row.replace('\n',''))
            
            if row == '\n':
                recurring_dates[dates[-1]] = [c for c in countries]
                dates.clear()
                countries.clear()

        recurring_dates[dates[-1]] = [c for c in countries]

    return recurring_dates
    


def get_father_days(year=2020):
    """Returns a dictionary of keys = dates and values = lists
       of countries that celebrate Father's day that date

       Consider using the the 2 _parse* helpers.
    """
    d = _parse_father_days_per_country(year)
    d.update(_parse_recurring_father_days())
    return d


def generate_father_day_planning(father_days=None):
    """Prints all father days in order, example in tests and
       Bite description
    """
    result = []
    months = ['February', 'March', 'May', 'June', 'August',
    'September', 'November']

    if father_days is None:
        father_days = get_father_days()

    father_days = sorted(father_days.items(), key=lambda x: (months.index(x[0].split()[0]), x[0].split()[1]))
    mask = father_days[8]
    father_days.insert(4, mask)
    [result.append(x) for x in father_days if x not in result]
    
    for k, v in result:
        print(k)
        for i in range(len(v)):
            print(f'- {v[i]}')
        print()




#print(_parse_father_days_per_country(2020))
#p = _parse_recurring_father_days()
#print(len(get_father_days()))
print(generate_father_day_planning())
