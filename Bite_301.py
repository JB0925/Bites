import os
from datetime import date
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve
import json
import calendar

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    thirty_one_days = '1 3 5 7 8 10 12'.split()
    thirty_days = '4 6 9 11'.split()
    February = 2
    smallest, biggest = None, None
    dates = [None]

    if start_date.month > end_date.month:
        smallest, biggest = end_date, start_date
    else:
        if start_date.day < end_date.day and start_date.month == end_date.month:
            smallest, biggest = start_date, end_date
        else:
            if start_date.month < end_date.month:
                smallest, biggest = start_date, end_date
            else:
                smallest, biggest = end_date, start_date
    
    
    years, days, months = smallest.year, smallest.day, smallest.month

    while dates[-1] != biggest:
        d = date(years, months, days)
        dates.append(d)
        days += 1
        if months == 12 and days == 32:
            years += 1
            months, days = 1, 1
        if str(months) in thirty_one_days and days == 32:
            months += 1
            days = 1
        if months == February and days == 30:
            months += 1
            days = 1
        if str(months) in thirty_days and days == 31:
            months += 1
            days = 1
    
    
    return dates[1:]
        


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    daily_rates = json.loads(RATES_FILE.read_text())['rates']
    rates = {}
    base_date = None
    dates_list = get_all_days(start, end)

    for row in daily_rates:
        if any(str(d) == row for d in dates_list):
            year, month, day = row.split('-')
            d = date(int(year), int(month), int(day))
            rates[d] = {'Base Date': d, 'GBP': daily_rates[row]['GBP'], 'USD': daily_rates[row]['USD']}
            
    
    for item in dates_list:
        try:
            if item in rates:
                base_date = item
            else:
                rates[item] = rates[base_date]
        except KeyError:
            pass
    
    return {k:v for k, v in sorted(rates.items())}



def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    
    if start_date < '2020-01-01' or end_date > '2020-09-01':
        raise ValueError ('One or both of your dates are not within the range of the dataset')
    
    final_rates = {}
    syear, smonth, sday = start_date.split('-')
    eyear, emonth, eday = end_date.split('-')
    start_date = date(int(syear), int(smonth), int(sday))
    end_date = date(int(eyear), int(emonth), int(eday))
    all_rates = match_daily_rates(start_date, end_date, RATES_FILE)
    
    if start_date not in all_rates:
        with open(RATES_FILE) as f:
            reader = json.load(f)
            base_date = date(2019, 12, 31)
            if start_date not in final_rates:
                final_rates[start_date] = {'Base Date': base_date, 'GBP': reader['rates']['2019-12-31']['GBP'],\
                    'USD': reader['rates']['2019-12-31']['USD']}
                
    all_rates.update(final_rates)
    return {k:v for k, v in sorted(all_rates.items())}
    
    
if __name__ == '__main__':
    first, second = "2020-01-01", "2020-09-01"
    print(exchange_rates(first, second))
